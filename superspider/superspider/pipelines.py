# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.exceptions import DropItem
import time
import MySQLdb
import MySQLdb.cursors
import socket
import select
import sys
import os
import errno


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

class Write2MySQLStorePipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            host = "10.1.1.86",
            db = 'hmengine',
            user = 'hmtest',
            passwd = 'hmtest',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = False
        )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item

    def _conditional_insert(self, tx, item):
        if item.get('symptom'):
            tx.execute('insert into spider_qa (department, hospital, doc_name, ask_time, symptom, symptoms_desc)  \
            values (%s, %s, %s, %s, %s, %s)', (item['department'], item['hospital'], item['name'], item['time'], \
            item['symptom'], item['symptoms_desc']))

