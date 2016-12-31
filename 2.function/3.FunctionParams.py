'''
函数的参数
    定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，
    只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。

    Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

    位置参数
    默认参数
    可变参数
        在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
    关键字参数
        可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
    命名关键字参数
        对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。


    *args是可变参数，args接收的是一个tuple；
    **kw是关键字参数，kw接收的是一个dict。
'''


# 位置参数
# 我们先写一个计算x2的函数：
def power(x):
    return x * x


print(power(2))


# 4

# 默认参数
def test(x, y=2):
    return x * y;


print(test(2), test(2, 3))
# 4 6

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum
print(calc(1,2,3,4))
# 10

# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
# name: Michael age: 30 other: {}
person('Bob', 35, city='Beijing')
# name: Bob age: 35 other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer')
# name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

# tips:**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
# name: Jack age: 24 other: {'job': 'Engineer', 'city': 'Beijing'}

# 命名关键字参数 --> 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')
# Jack 24 Beijing Engineer