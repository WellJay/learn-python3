'''
调用函数
    Python内置了很多有用的函数，我们可以直接调用。

    要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。可以直接从Python的官方网站查看文档：

    函数大全：http://docs.python.org/3/library/functions.html

    基础函数：abs max
    数据类型转换：int('str') float('str') str(number) bool(1) bool('')
'''

# tips:也可以在交互式命令行通过help(abs)查看abs函数的帮助信息。
help(abs)
# abs(...)
#    abs(number) -> number
#   Return the absolute value of the argument.

print(abs(100), abs(-20), abs(12.34))
# 100 20 12.34

print(max(1, 2, -3))
# 2

print(int('123'))
# 123
print(int(12.34))
# 12
print(float('12.34'))
# 12.34
print(str(100))
# 100
print(bool(1), bool(''))
# True False

# tips:函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print(a(-1))
# 1