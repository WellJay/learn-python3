'''
使用list和tuple
- Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
- 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改。
- list [...]    tuple (...)
'''

family = ['father', 'mother', 'me', 'brother']
print(family)
# ['father', 'mother', 'me', 'brother']

# tips:这里的len就是计算list的size，并不是字符串长度
print(len(family))
# 4

print(family[0])
# father
print(family[2])
# me

# tips:当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。
# print(family[4])
# IndexError: list index out of range

# tips:如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print(family[-1])
# brother

# tips:list是一个可变的有序表，所以，可以往list中追加元素到末尾,也可以把元素插入到指定的位置，比如索引号为1的位置
family.append('sister')
print(family)
# ['father', 'mother', 'me', 'brother', 'sister']

family.insert(1, 'others')
print(family)
# ['father', 'others', 'mother', 'me', 'brother', 'sister']


# tips:要删除list末尾的元素，用pop()方法, 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
family.pop()
print(family)
# ['father', 'others', 'mother', 'me', 'brother']

family.pop(1)
print(family)
# ['father', 'mother', 'me', 'brother']

# tips:要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
family[0] = 'grandfather'
print(family)
# ['grandfather', 'mother', 'me', 'brother']

# tips:list里面的元素的数据类型也可以不同，list元素也可以是另一个list
L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
# 4


# ============================tuple==============================
# tuple一旦初始化就不能修改

classmates = ('Michael', 'Bob', 'Tracy')
# tips:classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素
# tips:不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
