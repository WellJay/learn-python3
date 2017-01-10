'''
    Base64是一种用64个字符来表示任意二进制数据的方法。

    用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法显示和打印的字符，
    所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。Base64是一种最常见的二进制编码方法。
    Base64的原理很简单，首先，准备一个包含64个字符的数组：

    ['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']

    Python内置的base64可以直接进行base64的编解码：
'''
import base64

a = base64.b64encode(b'test')
print(a)
# b'dGVzdA=='
print(base64.b64decode(a))
# b'test'
'''
    由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
'''
b = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(b)
# b'abcd++//'
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
# b'abcd--__'
