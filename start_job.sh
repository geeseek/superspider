#/bin/bash
./gen_proxy.sh;
cd superspider;
mkdir -p jobs/$1;
#/usr/local/bin/scrapy crawl $1 -s JOBDIR=jobs/$1 -L WARNING &> ~/log.txt; 
/usr/local/bin/scrapy crawl $1 -s JOBDIR=jobs/$1 &> ~/log.txt 
cd -;
