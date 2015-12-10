#coding:utf-8

# load requests-module, a streamlined http-client lib
import requests

# load posters encode-function
from poster.encode import multipart_encode



# an adapter which makes the multipart-generator issued by poster accessable to requests
# based upon code from http://stackoverflow.com/a/13911048/1659732
class IterableToFileAdapter(object):
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.length = iterable.total

    def read(self, size=-1):
        return next(self.iterator, b'')

    def __len__(self):
        print self.length
        return self.length

# define a helper function simulating the interface of posters multipart_encode()-function
# but wrapping its generator with the file-like adapter
def multipart_encode_for_requests(params, boundary=None, cb=None):
    datagen, headers = multipart_encode(params, boundary, cb)
    return IterableToFileAdapter(datagen), headers



# this is your progress callback
def progress(param, current, total):
    if not param:
        return

    # check out http://tcd.netinf.eu/doc/classnilib_1_1encode_1_1MultipartParam.html
    # for a complete list of the properties param provides to you
    print "{0} ({1}) - {2:d}/{3:d} - {4:.2f}%".format(param.name, param.filename, current, total, float(current)/float(total)*100)

# generate headers and gata-generator an a requests-compatible format
# and provide our progress-callback
datagen, headers = multipart_encode_for_requests({
    'piczip':open(r'D:\tools\workspacePy\test\upload\resource.zip', mode='rb'),'utype':1,'uid':'12345','title':u'第二个故事','coverPic':'pic.jpg','templateId':'1','musicState':'0','pages':[{"picture": "aaa.jpg","text": "2015故事%^&","serialNo": 1 }, {"picture": "bbb.jpg","text": "fff","serialNo": 2 },{"picture": "ccc.jpg","text": "cc","serialNo": 3 }]}, cb=progress)

# use the requests-lib to issue a post-request with out data attached

"""
res = urllib2.Request('http://story-test.tclclouds.com/api/savestory?',datagen,headers)
res.add_data(data)
r= urllib2.urlopen(res)

print r,r.read()


"""

post_data= {"utype":1,
            "uid":"12345",
            "title":u"第二个故事",
            "coverPic":"pic.jpg",
            "templateId":"1",
            "musicState":"0",
            "pages":[{"picture": "aaa.jpg","text": "2015故事%^&","serialNo": 1 }, {"picture": "bbb.jpg","text": "fff","serialNo": 2 },{"picture": "ccc.jpg","text": "cc","serialNo": 3 }]}

r = requests.post(
    'http://story-test.tclclouds.com/api/savestory?',
    data=datagen,
    headers=headers
)


# show response-code and -body
print r,r.text