'''
filter过滤器
'''
'''
    过滤偶数
'''


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
# [1, 5, 9, 15]

'''
    把一个序列中的空字符串删掉，可以这么写：
'''


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
# ['A', 'B', 'C']
