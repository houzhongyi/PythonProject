import chardet
data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))


print(chardet.detect('离离原上草，一岁一枯荣'.encode('gbk')))