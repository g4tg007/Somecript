#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import json
import sys
from nti_api import handle_api
import argparse



def list_args():
	
	parser = argparse.ArgumentParser()
	parser.add_argument("--index","-i",default='ve')
	parser.add_argument("--query","-q",default='*')
	parser.add_argument("--startTime","-sT",default='2017-06-15')
	parser.add_argument("--endTime","-eT")
	parser.add_argument("--size","-z",default='10')
	parser.add_argument("--page","-p")
	parser.add_argument("--format","-f",action="store_true",default=False)
	args = parser.parse_args()

	str_args=[]
	if args.index:
		str_args.append("index="+args.index)

	if args.query:
		str_args.append("query=\""+args.query+"\"")

	if args.startTime:
		str_args.append("startTime="+args.startTime)

	if args.endTime:
		str_args.append("endTime="+args.endTime)

	if args.size:
		str_args.append("size="+args.size)

	if args.page:
		str_args.append("page="+args.page)
	if args.format:
		global format
		format=args.format

	return str_args

if __name__ == '__main__':
	argvs=list_args()
	api=handle_api()
	data=api.send("1",argvs)
	if format is True:
		data=json.dumps(data, indent=4, sort_keys=False, ensure_ascii=False)
		pass
	print data
