#coding:utf-8

import sys
p = r'D:\tools\workspacePy\测试'
sys.path.append(p.decode('utf8').encode('gb2312'))
print sys.path
from common.utils import person

if __name__ == '__main__':
    p = person()
