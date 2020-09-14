#!/usr/bin/env python
# -*- coding: utf-8 -*-
from jingdong.spiders.jd_comment import run_master
if __name__ == '__main__':
    run_master(retry=True, spider_num=200)

