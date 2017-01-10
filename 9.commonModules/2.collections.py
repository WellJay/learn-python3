'''
集合

    collections是Python内建的一个集合模块，提供了许多有用的集合类。

    namedtuple
    我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：
'''
p = (1, 2)
'''
    但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。

    定义一个class又小题大做了，这时，namedtuple就派上了用场：
'''
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)

'''
    deque

    使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
    deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
'''
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
# deque(['y', 'a', 'b', 'c', 'x'])

'''
    defaultdict

    使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
'''
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
print(dd['key2'])
# N/A


'''
    Counter

    Counter是一个简单的计数器，例如，统计字符出现的个数：
'''
from collections import Counter

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
# Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'n': 1, 'i': 1, 'a': 1})
