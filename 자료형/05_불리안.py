'''
bool(?)
참이면 True
거짓이면 False
값이 있으면 True
값이 없으면 False
'''

a = 'hello' #값이 있음 o
b = '  '    #값이 있음 o
c = ''      #값이 없음 x
print(bool(a))
print(bool(b))
print(bool(c))
print()

a = 1   #값이 있음 o
b = -2  #값이 있음 o
c = 0   #값이 없음 x
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(None)) #값이 없음 x