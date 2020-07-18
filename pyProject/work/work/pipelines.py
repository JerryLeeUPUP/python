# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import csv


class WorkPipeline(object):
    def __init__(self):
        # csv文件路径
        store_file = os.path.dirname(__file__) + '/spiders/result.csv'
        print("***************************************************************")
        # 打开(创建)文件
        self.file = open(store_file, 'w+')
        # csv写法
        self.writer = csv.writer(self.file)

    def process_item(self, item, spider):
        if item['code'][-2:] == '58':
            self.writer.writerow((item['code'], item['name']))
        return item

    def close_spider(self, spider):
        # 关闭爬虫时顺便将文件保存退出
        self.file.close()
