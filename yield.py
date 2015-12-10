#coding:utf-8

import urllib2,urllib

data = {'name':'test'}

rs = urllib.urlencode(data)
print urllib2.urlopen('http://www.baidu.com',rs)
