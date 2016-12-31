'''
循环是让计算机做重复任务的有效的方法。

break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。

要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。

有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。

for var in vars:
    do something

while conditional:
    if conditional is true do something

break    中断结束循环
continue 跳出当前这一次循环,直接开始下一次循环。
'''

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
# Michael
# Bob
# Tracy

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
# 55

# tips:如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
print(list(range(5)))
# [0, 1, 2, 3, 4]

sum = 0
for x in range(101):
    sum = sum + x
print(sum)
# 5050

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
# 2500

for x in range(50):
    if x == 2:
        break
    else:
        print(x)
# 0
# 1

for x in range(4):
    if x == 2:
        continue
    else:
        print(x)
# 0
# 1
# 3
