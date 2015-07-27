#/bin/bash
curl 'http://revx.daili666.com/ip/?tid=556617812511460&num=50&protocol=http&category=2' > proxy_list.txt;
sed -i 's/^/http:\/\//g' proxy_list.txt;
cp proxy_list.txt  superspider/proxy_list.txt;
#cat proxy_list.txt >> superspider/proxy_list.txt;
