import whois
import urllib2
# print whois.whois("appspot.com")
# def download(url):
#     print 'Downloading:', url
#     try:
#         html = urllib2.urlopen(url).read()
#     except urllib2.URLError as e:
#         print 'Download error:', e.reason
#         html = None
#     return html
#reload
def download(url, num_retries=2):
    print 'Downloading:', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries-1)
    return html


print download("http: //httpstat. us/500")

