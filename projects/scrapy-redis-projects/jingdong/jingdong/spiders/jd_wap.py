#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from multiprocess.scrapy_redis.spiders import JiChengSpider


class JDComment(JiChengSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'jd_comment'
    allcnt_pattern = re.compile(r'"commentCount":(\d+),')

    def parse(self, response):
        if response._status == 0 and response.text:
            count = self.allcnt_pattern.findall(response.text)
            if not count:
                yield {"skuid": response.meta["_seed"], "comment": "0", }
            else:
                yield {"skuid": response.meta["_seed"], "comment": str(count[0])}
        else:
            yield {}


