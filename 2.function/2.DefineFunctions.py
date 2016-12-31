'''
定义函数
    在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。

    请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
    如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
    return None可以简写为return。

    空函数
        如果想定义一个什么事也不做的空函数，可以用pass语句：
        pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

    返回多个值
        函数可以返回多个值吗？答案是肯定的。
        比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标
        但其实这只是一种假象，Python函数返回的仍然是单一值：
        原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
'''


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-5))


def nop():
    pass


nop()

age = 15
if age >= 18:
    pass


# tips:函数参数检查。错误和异常处理将在后续讲到。
def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# my_abs('A')
# TypeError: unorderable types: str() >= int()


# tips: the real is return a tuple value;
def return_2_value():
    return 1, 2


a, b = return_2_value()
print(a, b);
# 1 2
