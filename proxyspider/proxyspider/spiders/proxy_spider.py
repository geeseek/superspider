import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from proxyspider.items import ProxyItem 

class ProxySpider(CrawlSpider):
    name = "proxy"
    allowed_domains = ["proxy.com.ru"]
    start_urls = ["http://www.proxy.com.ru/list_1.html",
                  "http://www.proxy.com.ru/list_2.html",
                  "http://www.proxy.com.ru/list_3.html",
                  "http://www.proxy.com.ru/list_4.html",
                  "http://www.proxy.com.ru/list_5.html"
                 ]
    rules = (
        Rule(LinkExtractor(allow=('list_[0-5]+.htm', )),  callback='parse_item'),
            ) 

    def parse_item(self, response):
        items = []
        for sel in response.xpath('//table/tbody/tr'):
            item = ProxyItem()
            ip = sel.xpath('td[2]').extract().encode('utf-8')     
            port = sel.xpath('td[3]').extract().encode('utf-8')     
            item['record'] = "".join("http://", ip, ":", port);
            print item['record']
            items.append(item)
        return items 

    def _process_request(self, request):  
        info('process ' + str(request))  
        return request  
