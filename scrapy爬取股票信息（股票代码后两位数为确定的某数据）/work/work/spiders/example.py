# -*- coding: utf-8 -*-
import json

import scrapy

from scrapy import Request
from work.items import WorkItem


class ExampleSpider(scrapy.Spider):
    name = 'eastmoney'
    allowed_domains = ['47.push2.eastmoney.com']

    # start_urls = ['http://quote.eastmoney.com/center/gridlist.html#hs_a_board']

    def start_requests(self):
        url = 'http://47.push2.eastmoney.com/api/qt/clist/get?pn=1&pz=20&po=1&np=1&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f12,f14'
        yield Request(url, callback=self.parse)

    def parse(self, response):
        print("开始")
        self.parse_data(response)
        for i in range(2, 201):
            url = 'http://47.push2.eastmoney.com/api/qt/clist/get?pn=' + str(i) + '&pz=20&po=1&np=1&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f12,f14'
            yield Request(url, callback=self.parse_data)
        print("结束")
        pass

    def parse_data(self, response):
        print("解析数据")
        data = json.loads(response.body)['data']['diff']
        for col in data:
            item = WorkItem()
            item['code'] = col['f12']
            item['name'] = col['f14']
            yield item
