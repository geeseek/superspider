import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from superspider.items import QAItem 

class QASpider(CrawlSpider):
    name = "qa"
    allowed_domains = ["haodf.com"]
    start_urls = ["http://zixun.haodf.com/index/13.htm",
                  "http://zixun.haodf.com/index/14.htm",
                  "http://zixun.haodf.com/index/15.htm",
                  "http://zixun.haodf.com/index/16.htm",
                  "http://zixun.haodf.com/index/17.htm",
                  "http://zixun.haodf.com/index/18.htm",
                  "http://zixun.haodf.com/index/19.htm",
                  "http://zixun.haodf.com/index/20.htm",
                  "http://zixun.haodf.com/index/21.htm",
                  "http://zixun.haodf.com/index/22.htm",
                  "http://zixun.haodf.com/index/23.htm",
                  "http://zixun.haodf.com/index/24.htm",
                  "http://zixun.haodf.com/index/25.htm",
                  "http://zixun.haodf.com/index/26.htm",
                  "http://zixun.haodf.com/index/27.htm",
                  "http://zixun.haodf.com/index/28.htm",
                  "http://zixun.haodf.com/index/29.htm",
                  "http://zixun.haodf.com/index/30.htm",
                  "http://zixun.haodf.com/index/31.htm",
                  "http://zixun.haodf.com/index/32.htm",
                  "http://zixun.haodf.com/index/33.htm",
                  "http://zixun.haodf.com/index/34.htm"
                 ]
    rules = (
        Rule(LinkExtractor(allow=('/index/[0-9]+.htm', ))),
        Rule(LinkExtractor(allow=('/wenda/[a-z0-9_]+.htm', )),  callback='parse_item'),
            ) 

    def parse_item(self, response):
        item = QAItem()
        symptom = response.xpath('//h1[@class="fl f20 fn fyahei pl20 bdn"]/span/text()').extract()  
        symptoms_desc = "".join(response.xpath('//div[@class="h_s_info_cons"]/div[1]/text()').extract())
        time =  response.xpath('//div[@class="yh_l_times"]/text()').extract()
        hospital = response.xpath('//div[@class="space_b_picright"]/div[2]/div/p/a[1]/text()').extract()
        department = response.xpath('//div[@class="space_b_picright"]/div[2]/div/p/a[2]/text()').extract()
        name = response.xpath('//h3[@class="doc_name f22 fl"]/text()').extract()
        url = response.url;

        if (len(symptom) > 0 and len(symptoms_desc) and len(time) > 0 and len(hospital) > 0 
            and len(department) > 0 and len(name) > 0):
            item['symptom'] = symptom[0].encode('utf-8').replace('\n',' ') 
            item['symptoms_desc'] = symptoms_desc.encode('utf-8').replace('\n',' ') 
            item['time'] = time[0].encode('utf-8').replace('\n',' ') 
            item['hospital'] = hospital[0].encode('utf-8').replace('\n',' ') 
            item['department'] = department[0].encode('utf-8').replace('\n',' ') 
            item['name'] = name[0].encode('utf-8').replace('\n',' ')  
            item['url'] = url
        return item 

    def _process_request(self, request):  
        info('process ' + str(request))  
        return request  
