#!/usr/bin/env python
# -*- coding: utf-8 -*-
from projects.scrapy_redis_projects.jingdong.jingdong.spiders.jd_brand import run_master
if __name__ == '__main__':
    run_master(retry=False, spider_num=40)

