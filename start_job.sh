#/bin/bash
./gen_proxy.sh;
cd superspider;
mkdir -p jobs/$1;
scrapy crawl $1 -s JOBDIR=jobs/$1 -L WARNING;
cd -;
