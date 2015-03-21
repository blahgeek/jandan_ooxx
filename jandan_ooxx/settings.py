# -*- coding: utf-8 -*-

# Scrapy settings for jandan_ooxx project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'jandan_ooxx'

FILES_STORE = '/tmp'
ITEM_PIPELINES = {'jandan_ooxx.pipelines.SingleImagePipeline': 1}

SPIDER_MODULES = ['jandan_ooxx.spiders']
NEWSPIDER_MODULE = 'jandan_ooxx.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jandan_ooxx (+http://www.yourdomain.com)'
