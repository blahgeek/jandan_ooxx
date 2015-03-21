# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OoxxItem(scrapy.Item):
    url = scrapy.Field()
    path = scrapy.Field()
    vote_oo = scrapy.Field()
    vote_xx = scrapy.Field()
