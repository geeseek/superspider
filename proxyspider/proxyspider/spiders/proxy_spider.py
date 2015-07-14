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
        Rule(LinkExtractor(allow=('list_[0-5].htm', )),  callback='parse_item'),
            )

    def parse(self, response):
        items = []
        for sel in response.xpath('//table/tr'):
            item = ProxyItem()
            ip = sel.xpath('td[2]/text()').extract()
            port = sel.xpath('td[3]/text()').extract()
            if len(ip) > 0 and len(port) > 0:
                item['record'] = "http://" + ip[0] + ":" + port[0]
                items.append(item)
        return items

