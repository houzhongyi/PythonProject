import requests
# r = requests.get('http://www.douban.com/')
# status = r.status_code
# print('请求状态码：%s' %status)
# print('text: %s' %r.text)
# r = requests.get('https://www.douban.com/search', params={'q':'python','cat':'1001'})
# print('URL:%s' %r.url)
# print('TEXT:%s' %r.text)
r = r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())