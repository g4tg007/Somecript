#!/usr/bin/env python
#coding=utf-8
import urllib2;
import threading;
import sys;
import os;
import time;
from time import sleep,ctime
from random import randint

def outxt(file,hostip):
    hostip = '%s\n' %(hostip)
    fip = open(file,'a')
    fip.write(hostip)
    fip.close()

def runpl(domain,payloads):
    if not (str(domain)).startswith('http'):
        url = 'http://' + domain
    else:
        url = domain
    if url.endswith('/'):
        url = url.rstrip('/')
        #print url

    for payload in payloads:
        url += payload
        try:
            headers ={"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
            req = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(req, timeout=20)
            html = response.read()
        except Exception, e:
            pass;
        time.sleep(randint(10,40));
    pass

def pllist(file):
    payloads = []
    pf = open(file, 'r')
    for line in pf.readlines():
        payload = line.replace('\n', '').replace('\r', '')
        payloads.append(payload)
    pf.close()    
    return payloads
    pass

def makelist(file):
    items = []
    fd = open(file, 'r')
    for line in fd.readlines():
        item = line.replace('\n', '').replace('\r', '')
        items.append(item)
    fd.close()    
    return items

def checkit(domain,payloads,condition=''):
    if condition=='':
        oflie='ok.txt'
    else:
        oflie=condition+'.txt'
        pass
    if not (str(domain)).startswith('http'):
        url = 'http://' + domain
    else:
        url = domain
    if url.endswith('/'):
        url = url.rstrip('/')
        #print url
    payload = ":8080/"
    url += payload
    try:
        #url = 'http://www.baidu.com/'
        headers ={"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
        req = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(req, timeout=20)
        html = response.read()
        #print html
        if str(html).find(condition) >= 0:
            outxt(oflie,domain)
            print "-HHH" + '------' + domain
            runpl(domain)
            return [1, html]
    except Exception, e:
        pass


data = 0
def func(host,payloads,condition):
    global data
    #print host
    checkit(host,payloads,condition)
    #sys.exit(0)
    
def checkiplist(ifile,pfile,condition):
    payloads=pllist(pfile)
    fd = open(ifile)
    for line in fd:
        #line=fd.readline();
        item = line.replace('\n', '').replace('\r', '')
        t=threading.Thread(target=func,args=(item,payloads,condition,))
        t.start()
        time.sleep(0.009)
        while True:
            time.sleep(0.009)
            if(len(threading.enumerate()) < 300):
                break
    fd.close()    


if __name__ == "__main__":
　　x=test()
    if x==1:
        print '''Can't find file, check your file name'''
    else
　　checkiplist("ips.txt",payloads.txt,'xxoook')
