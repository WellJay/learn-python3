'''
dict
    Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
    和list比较，dict有以下几个特点：
        - 查找和插入的速度极快，不会随着key的增加而变慢；
        - 需要占用大量的内存，内存浪费多。
    而list相反：
        - 查找和插入的时间随着元素的增加而增加；
        - 占用空间小，浪费内存很少。
    所以，dict是用空间来换取时间的一种方法。
set
    set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
        - 通过add(key)方法可以添加元素到set中
        - 通过remove(key)方法可以删除元素
'''

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
# 95

# tips:把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['WellJay'] = 59
print(d)
# {'Tracy': 85, 'Michael': 95, 'Bob': 75, 'WellJay': 59}

# tips:如果key不存在，dict就会报错：
'''
d['Thomas']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Thomas'
'''

# tips:要避免key不存在的错误，有两种办法，一是通过in判断key是否存在，二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print('Thomas' in d)
# False
print(d.get('Thomas'))
# None

# tips:要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('WellJay')
print(d)
# {'Michael': 95, 'Bob': 75, 'Tracy': 85}


s = set([1, 2, 3])
print(s)
# {1, 2, 3}

# tips:重复元素在set中自动被过滤：
s = set([1, 1, 2, 2, 3, 3])
print(s)
# {1, 2, 3}

s.add(9)
s.remove(3)
print(s)
# {1, 2, 9}