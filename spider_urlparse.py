#coding=utf-8
import urlparse
url = set()
url.add('javascript:void(0)')
url.add('http://freebuf.com/geek')
url.add('https://freebuf.com:443/geek?id=1#sid')
url.add('ftp://freeme.com/ss/s/s')
url.add('sssfadea://ssss.ss')
url.add('//freebuf.com/s/s/s')
url.add('/freebuf.com/s/s/s/')
url.add('//freebuf.com/s/s/s/')
url.add('path/me')
url.add('path?ss=1')
url.add('path?ss=1&s=1')
url.add('path?ss=1#arch')
url.add('?ss=1')
url.add('#arch')
for item in url:
   print item
   o= urlparse.urlparse(item)
   print o