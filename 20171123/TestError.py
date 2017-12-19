# try:
#     print('try...')
#     r = 10 / 2
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')

try:
    print('try...')
    r = 10 / int('0')
    print('result:', r)
except BaseException as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('here')
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')