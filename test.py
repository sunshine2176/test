#coding:utf-8

import json
import re
import chardet
import urllib,urllib2

def te(*params):
    print u'中文中午',len(params)

def different(temp):
    if temp == 1:
        return True
    else:
        return '1111'
def recipients():
    """转换收件人地址"""
    #s = 'Xixi, QIN(MIE CD R&D VAL-CD-TCT) intern <xixi.qin@tcl.com>; Pengxia, WANG(MIE CD R&D VAL-CD-TCT) intern <pengxia.wang@tcl.com>; Lei, SUN(MIE CD R&D VAL-CD-TCT) <leisun@tcl.com>; Yang, LI(MIE CD R&D VAL-CD-TCT) intern <yang-li@tcl.com>; Zicheng, SUN(MIE CD R&D VAL-CD-TCT) <zicheng.sun@tcl.com>; Wei, YANG(MIE CD R&D VAL-CD-TCT) <wei.y@tcl.com>; Xinjiu, QIAO(MIE CD R&D VAL-CD-TCT) <xinjiu.qiao@tcl.com>; Liling, WANG(MIE CD R&D VAL-CD-TCT) <liling.wang@tcl.com>; Zhoupei, HE(MIE CD R&D VAL-CD-TCT) <zhoupei.he@tcl.com>; Tingting, HE(MIE CD R&D VAL-CD-TCT) <tingtinghe@tcl.com>; Zhanyu, HUO(MIE CD R&D VAL-CD-TCT) <zhanyu.huo@tcl.com>;Xiaobo, CHI(MIE CD R&D VAL-CD-TCT) <xiaobo.chi@tcl.com>'
    #s = 'Liechao, QING(MIE CD R&D CTD CD-CD-TCT) <liechao.qing@tcl.com>; Chao, ZHENG(MIE CD R&D CTD CD-CD-TCT) <chao.zheng@tcl.com>; Fei, WANG(MIE CD R&D CTD CD-CD-TCT) <fei_wang@tcl.com>; Lei, SUN(MIE CD R&D VAL-CD-TCT) <leisun@tcl.com>;Peng, WAN(MIE CD R&D PD-CD-TCT) <peng.wan@tcl.com>'
    s = 'Zhanyu, HUO(MIE CD R&D VAL-CD-TCT) <zhanyu.huo@tcl.com>;Lei, SUN(MIE CD R&D VAL-CD-TCT) <leisun@tcl.com>; Xiaobo, CHI(MIE CD R&D VAL-CD-TCT) <xiaobo.chi@tcl.com>; Wei, YANG(MIE CD R&D VAL-CD-TCT) <wei.y@tcl.com>'
    l = re.findall('<(.*?)>',s)
    r = ''
    for i in l:
        r = r + i + ';'
    print r

if __name__ == '__main__':
    try:
        print 1 + 'a'
    except:
        raise RuntimeError('fail')
    try:
        print 2 + 'b'
    except:
        raise RuntimeError('fail2')
    
    #sorted(d.iteritems,key = lambda c : c[0])
    #for k,v in d.iteritems():
    #    print k,v
    #recipients()
