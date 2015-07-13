import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from superspider.items import QAItem 

class QASpider(CrawlSpider):
    name = "qa"
    allowed_domains = ["haodf.com"]
    start_urls = ["http://zixun.haodf.com/index/1.htm",
                  "http://zixun.haodf.com/index/2.htm"
                 ]
    rules = (
        Rule(LinkExtractor(allow=('/index/[0-9]+.htm', ))),
        Rule(LinkExtractor(allow=('/wenda/[a-z0-9_]+.htm', )),  callback='parse_item'),
            ) 

    def parse_item(self, response):
        item = QAItem()
        item['symptom'] = (" ".join(response.xpath("//title/text()").extract())).encode('utf-8')     
        item['symptoms_desc'] = (" ".join(response.xpath("//div[@style='border-bottom:1px dashed #d2d2d2;font-size: 14px;line-height: 32px;margin-bottom: 8px;']/text()").extract())).encode('utf-8')
        return item 

    def _process_request(self, request):  
        info('process ' + str(request))  
        return request  
