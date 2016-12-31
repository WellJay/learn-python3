'''
列表生成式
    列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。


    举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
    list(range(1, 11))
    但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
    L = []
    for x in range(1, 11):
        L.append(x * x)

    但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
'''

# tips:写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
l = [x * x for x in range(1, 11)]
print(l)

# tips:筛选出仅偶数的平方
l = [x * x for x in range(1, 11) if x % 2 == 0]
print(l)

# tips:还可以使用两层循环，可以生成全排列
l = [m + n for m in 'ABC' for n in '123']
print(l)

# tips:运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os

files = [d for d in os.listdir('.')]
print(files)
# ['1.Slice.py', '2.Iteration.py', '3.ListComprehensions.py']

# tips:for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)
# z = C
# x = A
# y = B

d = {'x': 'A', 'y': 'B', 'z': 'C' }
l = [k + '=' + v for k, v in d.items()]
print(l)
# ['z=C', 'y=B', 'x=A']


# 最后把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s for s in L1 if isinstance(s, str)]
print(L2)
# ['Hello', 'World', 'Apple']