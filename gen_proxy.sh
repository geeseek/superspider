#/bin/bash
cd proxyspider;
scrapy crawl proxy;
cp proxy_list.txt ../;
cd -;
cp proxy_list.txt superspider/;
