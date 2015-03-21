# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JandanOoxxPipeline(object):
    def process_item(self, item, spider):
        return item

import scrapy
from scrapy.contrib.pipeline.files import FilesPipeline
from scrapy.exceptions import DropItem

class SingleImagePipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['url'])

    def item_completed(self, results, item, info):
        ok, x = results[0]
        if not ok:
            raise DropItem("Download image failed.")
        item['path'] = x['path']
        return item
