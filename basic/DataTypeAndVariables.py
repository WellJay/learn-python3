'''
数据类型和变量
- 整数   eg:1,100,-8888
- 浮点数 eg:1.23,-8,88
- 字符串 eg:"str",'test'
- 布尔   eg:True,False,2 > 1,1 == 1
- 空值   None
- 变量   eg:num = 5, age = 20
- 常量   eg:PI=3.14159265359
'''

# tips:转义字符\
print('I\'m ok.')
# I'm ok.

print('I\'m learning\nPython')
# I'm learning
# Python

print('\\\\')
# \\

# tips:如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容，
print('''line1
...line2
...line3''')
# lin1
# ...line2
# ...line3

print(True)
# True
print(2 > 1)
# True
print(True and False)
# False

# tips:条件判断
age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')
# adult

a = 'ABC'
b = a
a = 'DEF'
print(b)
# ABC
