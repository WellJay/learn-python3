'''
迭代
    如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
    在Python中，迭代是通过for ... in来完成的
'''

# tips:dist无序！！默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
# a
# b
# c
for value in d.values():
    print(value)
# 1
# 2
# 3

# tips:判断一个对象是否可以迭代
from collections import Iterable

print(isinstance('abc', Iterable), isinstance([1, 2, 3], Iterable), isinstance(123, Iterable))
# True True False