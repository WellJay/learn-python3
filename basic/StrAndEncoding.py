'''
字符串和编码
- 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
- 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
  Python对bytes类型的数据用带b前缀的单引号或双引号表示
- 以Unicode表示的str通过encode()方法可以编码为指定的bytes
- 格式化占位符 %d:整数 %f:浮点数 %s:字符串 %x:十六进制整数
'''

print("中文字符串")
# 中文字符串

print(ord('A'))
# 65
print(chr(97))
# a

# tips:要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节
x = b'ABC'
print(x)
# b'ABC'

print('TEST'.encode('ascii'))
# b'TEST'
print('中文'.encode('utf-8'))
# b'\xe4\xb8\xad\xe6\x96\x87'

# tips:要计算str包含多少个字符，可以用len()函数
print(len('ABC'))
# 3

print('Hello, %s' % 'world')
# Hello, world
