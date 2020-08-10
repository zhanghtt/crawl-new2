#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import os
import queue
import random
import re
from datetime import datetime

import lxml.html
import requests

import pymongo
import time


class PaginateException(BaseException):
    # download params error
    pass


class LiePin:

    def __init__(self):
        self.base_url = 'https://www.liepin.com/zhaopin/'
        self.db = pymongo.MongoClient('mongodb://192.168.0.13')['liepin']
        self.companyCol = time.strftime('company_%Y%m%d', time.localtime(time.time()))
        self.task_q = queue.Queue()
        self.reg_cmp_id = re.compile('.+company/(\d+)/')

    def download(self, task):
        """
        task: type -> dict
        cur_page(当前页): type -> int
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
            url, city_code, indus_code, cur_page = task['url'], task['city_code'], task['indus_code'], task['cur_page']
            # curPage: 爬虫页面控制参数，从0开始
            # d_pageSize=40 控制页面数量
            params = {'industries': indus_code, 'dqs': city_code, 'curPage': cur_page, 'd_pageSize': 40,
                      'fromSearchBtn': 2}
            response = requests.get(url, params=params, headers=headers, timeout=30)
            response.encoding = 'utf8'
            print('current_url -> {}'.format(response.url))
            time.sleep(random.uniform(1, 1.5))
            return response
        except Exception as e:
            # request 发生异常则将task重新放入队列中
            with open('./logs/http_error_logs', 'a') as g:
                g.write('{}\t{}\t{}\n'.format(str(e), task, time.ctime()))
            self.task_q.put(task)
            time.sleep(60)

    def html_page_parse(self, page, task):
        """
        在page中循环
        """
        result_list = []
        xml = lxml.html.fromstring(page)
        # 页面解析
        company_dom_list = xml.xpath(
            '//ul[@class="sojob-list"]/li/div[contains(@class, "sojob-item-main")]/div[contains(@class, "company-info")]')
        for dom in company_dom_list:
            company_name = dom.xpath('./p[@class="company-name"]/a/text()')
            company_url = dom.xpath('./p[@class="company-name"]/a/@href')
            try:
                company_id = self.reg_cmp_id.search(company_url[0]).group(1)
                company_info = {
                    'name': company_name[0].strip(),
                    'id': company_id,
                    'e_kind': '',
                    'industry': '',
                    'formdata': {'dq': task['city_code'], 'industry': task['indus_code']}
                }
                result_list.append(company_info)
            except IndexError:
                # 无公司id
                pass
        return result_list

    def get_url_params(self):
        # 按行业分类
        industries = []
        # 按地区分类
        cities = self.db.city.find_one({}, {"relations": 1})["relations"].keys()
        indus_query_result = self.db.industry.find_one({}, {"relations": 1})["relations"].values()
        [industries.extend(item) for item in indus_query_result]
        # 分类进行排列组合 count: 6936
        categories = itertools.product(cities, industries)
        for cate in categories:
            # 将任务放入队列中
            task = {'url': self.base_url, 'city_code': cate[0], 'indus_code': cate[1], 'cur_page': 0}
            self.task_q.put(task)
        # 获取队列任务数
        task_count = self.task_q.qsize()
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('{now} create {task_count} tasks'.format(now=now, task_count=task_count))

    def insert_into_mongo(self, items):
        self.db[self.companyCol].insert(items)

    def adsl(self):
        os.system('echo "jq123" | sudo -S poff')
        print('poff')
        time.sleep(5)
        os.system('pon dsl-provider')
        print('pon')
        time.sleep(10)

    def spider_start(self):
        # 加载任务
        self.get_url_params()
        with open('liepin_data', 'w') as g:
            while not self.task_q.empty():
                task = self.task_q.get()
                response = self.download(task)
                if not response:
                    continue
                # 判断是否有下一页进行添加
                if ('没有找到符合条件的职位' in response.text) or task['cur_page'] >= 100:
                    pass
                elif 'warning-msg' in response.text:
                    self.adsl()
                    self.task_q.put(task)
                else:
                    task['cur_page'] += 1
                    self.task_q.put(task)
                result_list = self.html_page_parse(response.text, task)
                # self.insert_into_mongo(result_list)
                # print(result_list)
                # 每页写入一次
                for company in result_list:
                    g.write('{}\t{}\t{}\t{}\n'.format(company['id'], company['name'], company['formdata']['dq'],
                                                      company['formdata']['industry']))
                    g.flush()


class FormatCompany:
    def __init__(self, filename):
        # format后的tablename
        self.table_name =  time.strftime('company_%Y%m%d',time.localtime(time.time()))
        self.new_company_lib = time.strftime('CompanyIdLib_%Y%m%d',time.localtime(time.time()))
        # company id库
        from mongo import op
        with op.DBManger() as m:
            last_company_ids = m.get_lasted_collection("liepin", filter={"name": {"$regex": r"CompanyIdLib_20\d\d\d\d\d\d"}})
        #self.company_ids = 'CompanyIdLib_20200602'
        self.company_ids = last_company_ids
        print("last_company_ids: " + last_company_ids)
        # 最终插入mongo的数据列表
        self.final_list = []
        # liepin_data
        self.filename = filename
        self.db = pymongo.MongoClient('mongodb://192.168.0.13:27017')['liepin']

    def read_file(self):
        """
        读取liepin_data并返回一个dict和一个set
        """
        temp_dict = {}
        temp_set = set()
        with open(self.filename, 'r') as g:
            for line in g.readlines():
                company_id, company_name, dq, indus = line.strip().split('\t')
                temp_dict.setdefault(company_id, {
                    'name': company_name,
                    'dq': dq,
                    'industry': indus
                    })
                temp_set.add(company_id)
        return temp_set, temp_dict

    def generate_new_company_ids(self, id_lib):
        """生成新的companyids库"""
        insert_dict = [{'_id': str(cid)} for cid in id_lib]
        self.db[self.new_company_lib].insert_many(insert_dict)

    def compare_and_insert(self):
        # company id 库
        company_ids = set(self.db[self.company_ids].distinct('_id'))
        new_company_ids, company_dict = self.read_file()

        # 生成新的companyidlib
        all_company_ids = company_ids.union(new_company_ids)
        self.generate_new_company_ids(all_company_ids)
        # insert ids
        # insert_ids = new_company_ids - company_ids
        # print(len(insert_ids))
        for cid in new_company_ids:
            temp = {
                'name': company_dict[cid]['name'],
                'industry': '',
                'id': cid,
                'e_kind': '',
                'formdata': {
                    'pagesize': 100,
                    'industry': company_dict[cid]['industry'],
                    'e_kind': 000,
                    'curPage': 0,
                    'keywords': '',
                    'dq': company_dict[cid]['dq']
                }
            }
            self.final_list.append(temp)
        # 插入数据
        self.db[self.table_name].insert_many(self.final_list)



# 先更新id库在更新companyALL_2 lib


class UpdateCompanyAll2:

    def __init__(self, companyCol):
        self.db = pymongo.MongoClient('mongodb://192.168.0.13')['liepin']
        #self.companyCol = time.strftime('company_%Y%m%d',time.localtime(time.time()))
        #self.companyCol = 'company_20200617'
        self.companyCol = companyCol
        self.collection_newcompany = self.db[self.companyCol]
        self.collection_company_all = self.db['companyALL_2']

    def get_new_companyids(self):
        new_ids = set(self.collection_newcompany.distinct('id'))
        old_ids = set(self.collection_company_all.distinct('_id'))
        insert_ids = list(new_ids - old_ids)
        return insert_ids

    def insert_into_companyALL2(self):

        insert_ids = self.get_new_companyids()
        print('total ids -> {}'.format(len(insert_ids)))
        new_company = []
        for cid in insert_ids:
            c = self.collection_newcompany.find_one({'id': cid})
            temp = {
                '_id': c['id'],
                'name': c['name'],
                'industry': c['formdata']['industry'],
                'e_kind': c['e_kind'],
                'dq': c['formdata']['dq']
                }
            #print(temp)
            new_company.append(temp)
        self.collection_company_all.insert_many(new_company)
        print('total -> {}'.format(len(new_company)))


if __name__ == '__main__':
    spider = LiePin()
    spider.spider_start()

    fc = FormatCompany("liepin_data")
    fc.compare_and_insert()

    u = UpdateCompanyAll2(fc.table_name)
    u.insert_into_companyALL2()
