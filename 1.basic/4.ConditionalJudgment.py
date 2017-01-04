'''
条件判断
if conditional:
    do something
elif conditional:
    do something
else:
    do something

input() - 接收值。中断程序，直到用户在终端中输入值，即可继续执行程序(值为str)
'''

age = 20
if age >= 18:
    print('you age is', age)
    print('adult')
# you age is 20
# adult


age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
# your age is 3
# teenager

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
# kid


s = input('please input your birth(请输入您的出生年份): ')
birth = int(s)  # str to int
if birth < 2000:
    print('00前')
else:
    print('00后')
