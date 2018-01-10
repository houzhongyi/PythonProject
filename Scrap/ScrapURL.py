#coding:utf-8
import os
import sys
import re
import urllib

URL_REG = re.compile(r'(http://[^/\\]+)', re.I)
# IMG_REG = re.compile(r'<img[^>]*?src=([\'"])([^\1]*?)\1', re.I)
IMG_REG = re.compile(r'<img src="http://(.*?)jpg"', re.I)

def download(dir, url):
    global URL_REG, IMG_REG
    m = URL_REG.match(url)
    if not m:
        print('[Error]Invalid URL:', url)
        return
    host = m.group(1)
    if not os.path.isdir(dir):
        os.mkdir(dir)
    html = urllib.urlopen(url).read().decode('gbk').encode('utf-8')
    print(re.findall(IMG_REG, html))
    imgs = [item[1].lower() for item in re.findall(IMG_REG, html)]
    f = lambda path: path if path.startswith('http://') else \
        host + path if path.startswith('/') else url + '/'
    imgs = list(set(map(f, imgs)))
    print('[Info]Find %d images.' %len(imgs))

    for idx, img in enumerate(imgs):
        name = img.split('/')[-1]
        path = os.path.join(dir, name)
        try:
            print('[Info]Download(%d): %s' %(idx + 1, img))
            urllib.urlretrieve(img, path)
        except:
            print("[Error]Can't download(%d): %s" %(idx + 1, img))

def main():
    if len(sys.argv) != 3:
        print('Invalid argument count.')
        return
    dir, url = sys.argv[1:]
    download(dir, url)

if __name__ == '__main__':
    download('D:\\Imgs', 'http://www.163.com')
    main()