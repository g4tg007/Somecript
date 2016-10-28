#coding=utf-8

import urllib

import sgmllib


class handle_html(sgmllib.SGMLParser):


 def unknown_starttag(self, tag, attrs):

    # 这里利用try与except来避免报错。

    # 但是并不推荐这样做，

    # 对于这种小脚本虽然无伤大雅，但是在实际的项目处理中，

    # 这种做法存在很大的隐患

    try:

        for attr in attrs:

            if attr[0] == "href":

                print attr[0]+":"+attr[1].encode('utf-8')

    except:

        pass


web = urllib.urlopen("http://freebuf.com/")

web_handler = handle_html()

web_handler.feed(web.read())
