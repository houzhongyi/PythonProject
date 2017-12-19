import urllib2
import cookielib

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://www.baidu.com')

for item in cookie:
    if item.name == "some_cookie_item_name":
        print (item.value)