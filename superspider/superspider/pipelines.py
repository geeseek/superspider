# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SuperspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class Write2TxtPipeline(object):
    def __init__(self):
        self.file = open('qa.txt', 'wb')

    def process_item(self, item, spider):
        line = item['department'] + "\t"
        line = line + item['hospital']  + "\t"
        line = line + item['name']  + "\t"
        line = line + item['time']  + "\t"
        line = line + item['symptom'] + "\t"
        line = line + item['symptoms_desc'] + "\t"
        line = line + "\n"
        self.file.write(line)
        return item

