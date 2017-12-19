import urllib.request
test = urllib.request.urlopen('http://www.baidu.com/')
print(test.read());