'''
返回函数

    函数作为返回值

    高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

    我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
'''


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


'''
    但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
'''


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum

'''
    当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
'''
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
# <function lazy_sum.<locals>.sum at 0x03064198>
'''
    调用函数f时，才真正计算求和的结果：
'''
print(f())