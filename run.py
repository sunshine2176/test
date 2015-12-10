#coding:utf-8

import urllib2

url = "http://watch.tclclouds.com/api/v1/relation/closeFriends/recommend?pageSize=7&pageNo=1"

headers = {"Authorization":"Bearer e0b37ee61c509925226d59cff08b1ed1","Content-Type":"application/json","Username":"polopheng@163.com"}
request = urllib2.Request(url,None,headers)
for k in headers:
   request.add_header(k,headers[k])

response = urllib2.urlopen(request)
print response.read()