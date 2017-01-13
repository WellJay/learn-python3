'''
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。

首先，我们看看itertools提供的几个“无限”迭代器：
'''
import itertools

# natuals = itertools.count(1)
# for n in natuals:
#     print(n)
# 1
# 2
# 3
# ...

cs = itertools.cycle('abc')  # 注意字符串也是序列的一种
# for c in cs:
#     print(c)
# a
# b
# c
# ...

'''
    repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
'''
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)
# A
# A
# A
'''
    无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。

    无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
'''
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
    chain()

    chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
'''
for c in itertools.chain('ABC', 'XYZ'):
    print(c)
# A
# B
# C
# X
# Y
# Z

'''
    groupby()
'''
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
    # A ['A', 'A', 'A']
    # B ['B', 'B', 'B']
    # C ['C', 'C']
    # A ['A', 'A', 'A']
