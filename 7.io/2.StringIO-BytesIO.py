'''
StringIO

    很多时候，数据读写不一定是文件，也可以在内存中读写。

    StringIO顾名思义就是在内存中读写str。

    要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
'''

from io import StringIO

f = StringIO()
f.write('hello')

f.write(' ')

f.write('world!')

# tips:getvalue()方法用于获得写入后的str。
print(f.getvalue())
# hello world!

'''
    要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
'''
from io import StringIO

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
# Hello!
# Hi!
# Goodbye!

'''
    BytesIO

    StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

    BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
'''
from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
# b'\xe4\xb8\xad\xe6\x96\x87'
'''
    请注意，写入的不是str，而是经过UTF-8编码的bytes。

    和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
'''
from io import BytesIO

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
# b'\xe4\xb8\xad\xe6\x96\x87'
