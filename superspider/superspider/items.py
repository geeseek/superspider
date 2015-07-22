# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QAItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    symptom = scrapy.Field()
    symptoms_desc = scrapy.Field()
    time = scrapy.Field() 
    hospital = scrapy.Field()
    department = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()

class HospitalItem(scrapy.Item):
    province = scrapy.Field()
    city = scrapy.Field()
    name = scrapy.Field()
    level = scrapy.Field()  

