import functools
import time

# sorted()排序
print('没有排序的列表：', [30, 12, 343, 1, 34, -1])
print('排序后的列表：', sorted([30, 12, 343, 1, 34, -1]))
print('绝对值排序：', sorted([23, -50, -1, 20, 200, -49], key=abs))
print('字母排序：', sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print('反向排序：', sorted(['bob', 'about', 'Zoo', 'Credit'], reverse=True, key=str.lower))

print('---------------------')

t = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[1]


print('按名字排序：', sorted(t, key=by_name))
print('成绩从高到低排序：', sorted(t, key=by_name, reverse=True))
print('---------------------')


# 返回函数
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createcounter():
    s = [0]

    def counter():
        s[0] += 1
        return s[0]

    return counter


# 测试:
counterA = createcounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createcounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

print('---------------------')


# 匿名函数
def is_odd(n):
    return n % 2 == 1


print('普通函数：', list(filter(is_odd, range(1, 20))))

print('匿名函数：', list(filter(lambda n: n % 2 == 1, range(1, 20))))

print('---------------------')


# 装饰器

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


now()
print('---------------------')


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2015-4-25')


now()

print('---------------------')


# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        timestamp = time.time()
        timearray = time.localtime(timestamp)
        otherstyletime = time.strftime("%Y--%m--%d %H:%M:%S", timearray)
        # print(otherstyletime)
        r = func(*args, **kw)
        print('%s excute in %s ' % (func.__name__, otherstyletime))
        return r

    return wrapper


@log
def fast(x, y):
    return x * y


fast(3, 5)

print('--------------------------')


# 偏函数
# base为做N进制的转换，默认值为10
# print(int('123', base=8))


# 转换成二进制字符串
def int2(x, base=2):
    return int(x, base)


print('二进制：', int2('110101'))

# 把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int3 = functools.partial(int, base=2)
print('二进制字符串:', int3('110101'))
