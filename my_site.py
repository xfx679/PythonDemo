import math


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(0))
print('--------------------------')


# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解。
def quadratic(a, b, c):
    m = b * b - 4 * b * c
    print(m)
    if m > 0:
        x = (-b + math.sqrt(m)) / (2 * a)
        y = (-b - math.sqrt(m)) / (2 * a)
        return x, y
    else:
        return 'no answer!'


print(quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
print('--------------------------')


# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(numbers):
    y = 1
    for x in numbers:
        y = y * x
        # print(y)
    return y


print(product([2, 2, 3, 4]))
print('---------------------------')


# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(10) =', fact(10))

print('---------------------------')


# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)  # 把上面n-1个从a-->b
        move(1, a, b, c)  # 把最下面一个从a-->c
        move(n - 1, b, a, c)  # 把上面n-1个从b-->c


move(4, 'A', 'B', 'C')
print('---------------------------')


# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：


def trim(s):
    print(len(s))
    if 0 == len(s):
        return s
    while ' ' == s[0]:
        s = s[1:]
        if 0 == len(s):
            return s
    while ' ' == s[-1]:
        s = s[:-1]
        if 0 == len(s):
            return s
    return s


# 测试:
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')
print(trim('  hello  world  '))

# s = 'hello  '
# leg = len(s)
# print(leg)
# print(s[0:leg-2])

print('---------------------------')

# 循环键
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

# 循环值
for value in d.values():
    print(value)
print('---------------------------')


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findminandmax(l):
    if l != []:
        mn, mx = (l[0], l[0])
        for x in l:
            if mx < x:
                mx = x
            if mn > x:
                mn = x
        return mn, mx
    else:
        return None, None


print(findminandmax([7, 2, 3, 5, 1]))

print('---------------------------')

b = range(1, 11)
print(b)
print(type(b))
print(list(b))

print('---------------------------')

a = [1, 2, 3, 4, 5, 6]
b = ['a', 'b', 'c', 'd', 'e', 'f']
c = [str(x) + str(y) for x, y in zip(b, a)]
print(c)

print('---------------------------')
g = (x * x for x in range(10))
for n in g:
    print(n)

print('---------------------------')

