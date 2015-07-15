import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from superspider.items import HospitalItem 

class HospitalSpider(CrawlSpider):
    name = "hospital"
    allowed_domains = ["haodf.com"]
    start_urls = [#"http://www.haodf.com/yiyuan/zhejiang/list.htm",
                  "http://www.haodf.com/yiyuan/beijing/chaoyang/list.htm",
                  "http://www.haodf.com/yiyuan/beijing/haidian/list.htm",
                  "http://www.haodf.com/yiyuan/beijing/xicheng/list.htm",
                  "http://www.haodf.com/yiyuan/beijing/dongcheng/list.htm",
                  "http://www.haodf.com/yiyuan/beijing/fengtai/list.htm",
                  "http://www.haodf.com/yiyuan/beijing/shijingshan/list.htm",
                  "http://www.haodf.com/yiyuan/beijing/daxing/list.htm",
                  "http://www.haodf.com/yiyuan/beijing/changping/list.htm",
                  "http://www.haodf.com/yiyuan/beijing/tongzhou/list.htm",
                  "http://www.haodf.com/yiyuan/beijing/fangshan/list.htm",
                  "http://www.haodf.com/yiyuan/beijing/huairou/list.htm",
                  "http://www.haodf.com/yiyuan/beijing/yanqing/list.htm",
                  "http://www.haodf.com/yiyuan/beijing/mentougou/list.htm",
                  "http://www.haodf.com/yiyuan/beijing/shunyi/list.htm",
                  "http://www.haodf.com/yiyuan/beijing/pinggu/list.htm"
                  "http://www.haodf.com/yiyuan/beijing/list.htm"
                 ]
    rules = (
        Rule(LinkExtractor(allow=('/yiyuan/zhejiang/[a-z]+/list.htm', )),  callback='parse_item'),
        Rule(LinkExtractor(allow=('/yiyuan/beijing/[a-z]+/list.htm', )),  callback='parse_item'),
            ) 

    def parse_item(self, response):
        items = []
        province = (response.xpath('//div[@class="kstl2"]/a/text()').extract()[0]).encode('utf-8')
        city = (response.xpath('//*[@id="el_result_content"]/div/div[3]/div/div[@class="m_title_green"]/text()').extract()[0]).encode('utf-8') 
        for sel in response.xpath('//*[@id="el_result_content"]/div/div[3]/div/div[2]/ul/li'):
            item = HospitalItem()
            item['province'] = province 
            item['city'] = city 
            item['name'] = (sel.xpath('a/text()').extract()[0]).encode('utf-8')
            item['level'] = (sel.xpath('span/text()').extract()[0]).encode('utf-8')
            items.append(item)
        return items

    def _process_request(self, request):  
        info('process ' + str(request))  
        return request  
