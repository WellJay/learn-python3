'''
调试
    程序能一次写完并正常运行的概率很小，基本不超过1%。总会有各种各样的bug需要修正。有的bug很简单，看看错误信息就知道，有的bug很复杂，我们需要知道出错时，哪些变量的值是正确的，
    哪些变量的值是错误的，因此，需要一整套调试程序的手段来修复bug。

    第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看：
'''


def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n


def main():
    foo('0')


# main()
# ZeroDivisionError: division by zero

'''
    断言
    凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
'''


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('0')


# main()
# AssertionError: n is zero!

'''
    logging
    print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
'''
import logging

s = '0'
n = int(s)
logging.info('n = %d' % n)
# print(10 / n)
# ZeroDivisionError: division by zero

'''
    IDE

    如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有PyCharm：

    http://www.jetbrains.com/pycharm/

    另外，Eclipse加上pydev插件也可以调试Python程序。
'''
