#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by i@BlahGeek.com at 2015-03-21

import re
import scrapy
from bs4 import BeautifulSoup
from jandan_ooxx.items import OoxxItem

class OoxxSpider(scrapy.Spider):
    name = "ooxx"
    allowed_domains = ["jandan.net"]
    start_urls = [
        "http://jandan.net/ooxx/page-1356",
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.body)
        commentlist = soup.find(class_='commentlist').findAll(id=re.compile('comment.*'), recursive=False)
        for comment in commentlist:
            vote_oo = comment.find(id=re.compile('cos_support.*')).text
            vote_xx = comment.find(id=re.compile('cos_unsupport.*')).text
            for img in comment.findAll('img'):
                item = OoxxItem()
                item['vote_oo'] = int(vote_oo)
                item['vote_xx'] = int(vote_xx)
                item['url'] = img['src']
                yield item
