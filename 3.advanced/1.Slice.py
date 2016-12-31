'''
切片
    取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：
    取前3个元素，应该怎么做？

    [start:end:length]

    在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单
'''

# 笨办法
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print([L[0], L[1], L[2]])
# ['Michael', 'Sarah', 'Tracy']


print(L[0:3])
# ['Michael', 'Sarah', 'Tracy']

# tips：如果第一个索引是0，还可以省略
print(L[:3])
# ['Michael', 'Sarah', 'Tracy']

# tips：也可以从索引1开始，取出2个元素出来
print(L[1:3])
# ['Sarah', 'Tracy']

# tips：类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，
print(L[-2:])
# ['Bob', 'Jack']
print(L[-2:-1])
# ['Bob']


L = list(range(100))
print(L[:10], L[-10:])
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

# tips:所有数，每5个取一个
print(L[::5])

# tips:字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
print('ABCDEFG'[:3])