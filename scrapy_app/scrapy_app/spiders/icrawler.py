# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import json


class IcrawlerSpider(CrawlSpider):
    name = 'icrawler'
    def __init__(self, *args, **kwargs):
        # We are going to pass these args from our django view.
        # To make everything dynamic, we need to override them inside __init__ method
        self.url = kwargs.get('url')
        self.word = kwargs.get('word')
        self.f = open('1.txt','w')
        self.start_urls = [self.url+ 'search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%s'%self.word+'&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%s'%self.word+'&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn=%d' %i for i in range(0,60,30)]

        IcrawlerSpider.rules = [
            Rule(LinkExtractor(unique=True), callback='parse'),
        ]
        super(IcrawlerSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        imgs = json.loads(response.body)['data']
        # print(len(imgs))
        for img in imgs:
            # print(img['middleURL'])
            self.f.write(img['middleURL']+'\n')

