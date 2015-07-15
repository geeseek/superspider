# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ProxyspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class Write2TxtPipeline(object):
    def __init__(self):
        self.file = open('proxy_list.txt', 'wb')

    def process_item(self, item, spider):
        line = item['record'] + "\n"
        self.file.write(line)
        return item


