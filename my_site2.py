from collections.abc import Iterable
from functools import reduce


# 生成器
def fib(mx):
    n, a, b = 0, 0, 1
    while n < mx:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# for x in fib(10):
#     print(x)

f = fib(10)
while True:
    try:
        y = next(f)
        print(y)
    except StopIteration as e:
        print('生成器返回值：%s' % e.value)
        break
print('-------------------------')

# 迭代器
# 判断对象是否是Iterable对象：
print('列表：', isinstance([], Iterable))
print('字典：', isinstance({}, Iterable))
print('字符串：', isinstance('str', Iterable))
print('生成器：', isinstance((x for x in range(10)), Iterable))
print('数字：', isinstance(100, Iterable))

print('-------------------------')


def f(x):
    return x * x


# map
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

print('-------------------------')

print(list(map(str, [1, 2, 3, 4, 5, 6, 7])))

print('-------------------------')


# reduce
# def add(x, y):
#     return x + y
#
#
# print(reduce(add, [1, 2, 3, 4, 5, 6]))
# print('-------------------------')


# def fn(x, y):
#     return x * 10 + y
#
#
# print(reduce(fn, [1, 3, 5, 7, 9]))
#
# print('-------------------------')


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']：

# upper字母变成大写，lower字母变成小写
def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name


print(list(map(normalize, ['adam', 'LISA', 'barT'])))

print('-------------------------')


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5, 6]))


def prod(L):
    return reduce(lambda x, y: x * y, L)


print(prod([3, 5, 7, 9]))

print('-------------------------')


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点def 数123.456：

def str2float(s):
    def fn(x, y):
        return x * 10 + y

    def floatnum(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    # 得到字符串中.的索引
    n = s.index('.')
    # 根据.的位置将字符串切片为两段
    s1 = list(map(int, [x for x in s[: n]]))
    s2 = list(map(int, [x for x in s[n + 1:]]))
    # m ** n表示m的n次方
    return reduce(fn, s1) + reduce(fn, s2) / 10 ** len(s2)


# 测试结果是否正确
print('str2float(\'123.456\')=', str2float('123.456'))

print('-------------------------')

arr = [0] * 10
k = 0
for i in range(10):
    arr[i] = i
for i in range(1, 4):
    k += arr[i] + 1
print(k)
print('-------------------------')


# filter()  过滤序列

def is_add(n):
    return n % 2 == 1


print(list(filter(is_add, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

print('-------------------------')


# 刪除末尾空字符

def not_empty(s):
    return s and s.strip()


print('原来的列表：', list(map(not_empty, ['a', 'b', '', 'c', ''])))
print('刪除末尾空字符的列表：', list(filter(not_empty, ['a', 'b', ''])))


def quans_empty(s):
    for a in s:
        if a == '':
            s.remove(i)
    return s


print('原来的列表：', list(map(quans_empty, ['1', '2', '3', '', '', 'a', '', 'c', 'b'])))
print('刪除所有空字符的列表：', list(filter(quans_empty, ['1', '2', '3', '', '', 'a', '', 'c', 'b'])))

print('-------------------------')


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

def is_palindrome(n):
    s = str(n)
    for x in range(len(s)):
        if s[x] == s[len(s) - 1 - x]:
            return n
        else:
            return False


print('原来的列表：',  [12321, 909, 213, 505, 34643, 34324])
print('过滤后的列表：', list(filter(is_palindrome, [12321, 909, 213, 505, 34643, 34324])))
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')