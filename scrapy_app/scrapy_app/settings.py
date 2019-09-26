# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_app project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import os
import sys

# DJANGO INTEGRATION

sys.path.append(os.path.dirname(os.path.abspath('.')))
# Do not forget the change iCrawler part based on your project name
os.environ['DJANGO_SETTINGS_MODULE'] = 'TestBaiduImg.settings'

# This is required only if Django Version > 1.8
import django

django.setup()

# DJANGO INTEGRATION

## Rest of settings are below ..

BOT_NAME = 'scrapy_app'

SPIDER_MODULES = ['scrapy_app.spiders']
NEWSPIDER_MODULE = 'scrapy_app.spiders'


USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0'

# # 下载图片的pipelines scrapy都做好了
# ITEM_PIPELINES = {
# 'scrapy.pipelines.images.ImagesPipeline': 1,
# }
#
# # items 中图片的url
# IMAGES_URLS_FIELD = 'image_urls'
# # .代表当前路径
# IMAGES_STORE = '.'


# # Crawl responsibly by identifying yourself (and your website) on the user-agent
# #USER_AGENT = 'scrapy_app (+http://www.yourdomain.com)'
#
# # Obey robots.txt rules
# ROBOTSTXT_OBEY = True
#
#
# ITEM_PIPELINES = {
#     'scrapy_app.pipelines.ScrapyAppPipeline': 300,
# }
