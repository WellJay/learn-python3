'''
日期时间

    datetime是Python处理日期和时间的标准库。
'''

'''
    获取当前日期和时间:
'''
from datetime import datetime

now = datetime.now();
print(now)
# 2017-01-10 11:23:30.044099
print(type(now))
# <class 'datetime.datetime'>
'''
    注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。

    如果仅导入import datetime，则必须引用全名datetime.datetime。

    datetime.now()返回当前日期和时间，其类型是datetime。



    获取指定日期和时间

    要指定某个日期和时间，我们直接用参数构造一个datetime：
'''
dt = datetime(2017, 1, 1, 12, 20)
print(dt)
# 2017-01-01 12:20:00

'''
    datetime转换为timestamp

    在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
    记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
'''
print(dt.timestamp())
# 1483244400.0

'''
    timestamp转换为datetime

    要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：
'''
t = 1429417200.0
print(datetime.fromtimestamp(t))
# 2015-04-19 12:20:00

'''
    str转换为datetime

    很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
'''
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
# 2015-06-01 18:19:59
'''
    datetime转换为str

    如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：
'''
print(now.strftime('%a, %b %d %H:%M'))
# Tue, Jan 10 12:05

'''
    datetime加减

    对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
'''
from datetime import timedelta

print(now + timedelta(hours=10))
# 2017-01-10 22:07:07.264003
print(now - timedelta(days=1))
# 2017-01-09 12:06:55.732436
