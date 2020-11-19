#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import sys

from fake_useragent import UserAgent

from mongo import op
from multiprocess.core.spider import SpiderManger
from multiprocess.tools import process_manger
from multiprocess.tools import timeUtil

current_date = timeUtil.current_time()
from multiprocess.tools.collections import TopK
import json
from multiprocess.core.spider import Seed
import requests


class JDPrice(SpiderManger):
    allcnt_pattern = re.compile(r'"commentCount":(\d+),')
    comments_pattern = re.compile(r'"comments":(\[.*\])')

    def __init__(self, **kwargs):
        super(JDPrice, self).__init__(**kwargs)
        self.ua = UserAgent()
        with op.DBManger() as m:
            #创建临时表本月任务的分界线
            m.create_db_collection(db_collection=("jingdong","jdcommentdetail{0}_sep".format(current_date)))
            skuid_set = {}
            top1000w = TopK(1)
            #skuids in last result
            last_result = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^summary_201905_20\d\d\d\d$"}})
            pipeline = [
                {
                    "$project": {
                        "skuid": "$skuid",
                        "comment_{}".format(last_result[-6:]):"$comment_{}".format(last_result[-6:])
                    }
                },
                {"$limit": 100}
            ]
            for item, comments in m.read_from(db_collect=("jingdong", last_result), out_field=("skuid","comment_{}".format(last_result[-6:])),pipeline=pipeline):
                if int(item) not in skuid_set:
                    top1000w.push(int(comments))
                    skuid_set[int(item)] = int(comments)
            top1000w = set(top1000w.get_topk())
            for i, seed in enumerate(skuid_set):
                if skuid_set[seed] in top1000w:
                    seed = Seed(value=seed, type=0)
                    self.seeds_queue.put(seed)

    def make_request(self, seed):
        price_address = "https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98" \
                  "&productId={0}&score=0&sortType=6&page=0&pageSize=10&isShadowSku=0&fold=1".format(seed.value)
        request = {"url": price_address,
                   "timeout": self.kwargs.get("request_timeout", 10),
                   "method": "get",
                   "sleep_time": 2,
                   "proxies": {"http": self.current_proxy},
                   "headers": {"Connection": "keep-alive", "User-Agent": self.ua.chrome,"Referer": "https://item.jd.com"}}
        return request

    def parse_item(self, content, seed):
        skuid = seed.value
        print(skuid)
        try:
            count = self.allcnt_pattern.findall(content)
            for item in json.loads(self.comments_pattern.findall(content)[0]):
                yield {"id": item.get("id"), "creationTime": item.get("creationTime"),
                       "discussionId": item.get("discussionId"), "referenceId": item.get("referenceId"),
                       "referenceTime": item.get("referenceTime"), "nickname": item.get("nickname")}
            maxpagesindex = max(0, min((int(count[0]) - 1) // 10, 99))
            print(maxpagesindex)
            for pindex in range(maxpagesindex + 1):
                url = "https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98" \
                      "&productId={0}&score=0&sortType=6&page={1}&pageSize=10&isShadowSku=0&fold=1".format(skuid,
                                                                                                           pindex)
                request = {"url": url,
                           "timeout": self.kwargs.get("request_timeout", 10),
                           "method": "get",
                           "sleep_time": 2,
                           "proxies": {"http": self.current_proxy},
                           "headers": {"Connection": "keep-alive", "User-Agent": self.ua.chrome,"Referer": "https://item.jd.com"}}
                respone = self.do_request(request)
                if respone and respone.status_code == requests.codes.ok:
                    if respone.text:
                        for item in json.loads(self.comments_pattern.findall(respone.text)[0]):
                            if item.get("creationTime") and item.get("creationTime") > "2020-05-01 00:00:00":
                                print({"id": item.get("id"), "creationTime": item.get("creationTime"),
                                   "discussionId": item.get("discussionId"), "referenceId": item.get("referenceId"),
                                   "referenceTime": item.get("referenceTime"), "nickname": item.get("nickname"),
                                   "userClient": item.get("userClient")})
                                self.write({"id": item.get("id"), "creationTime": item.get("creationTime"),
                                   "discussionId": item.get("discussionId"), "referenceId": item.get("referenceId"),
                                   "referenceTime": item.get("referenceTime"), "nickname": item.get("nickname"),
                                   "userClient": item.get("userClient")})
                        seed.ok()
                    else:
                        self.log.info("because: response.text is {}, url is {}, proxy is {}".format(respone.text,
                                                                                                    url,self.current_proxy))
        except Exception as e:
            e.__repr__()
            self.log.exception(e)


if __name__ == "__main__":
    current_date = timeUtil.current_time()
    process_manger.kill_old_process(sys.argv[0])
    import logging
    from multiprocess.core import HttpProxy
    config = {"job_name": "jdcommentdetail"
              , "spider_num": 1
              , "retries": 10
              , "request_timeout": 10
              , "complete_timeout": 5*60
              , "sleep_interval": 1
              , "rest_time": 5
              , "write_seed": False
              , "mongo_config": {"addr": "mongodb://192.168.0.13:27017", "db": "jingdong", "collection": "jdcommentdetail{}retry1".format(current_date)}
              , "log_config": {"level": logging.INFO, "filename": sys.argv[0] + '.logging', "format":'%(asctime)s - %(filename)s - %(processName)s - [line:%(lineno)d] - %(levelname)s: %(message)s'}
              ,"proxies_pool": HttpProxy.getHttpProxy()}
    p = JDPrice(**config)
    p.main_loop(show_process=True)
