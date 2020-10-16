# from random import randint

# a = 10;
# end=""是不换行的意思
# for a in range(0, 1):
#     for b in range(97, 123):
#         print(b, end="")

# QQ号码
# qq_number = "1234567"
#
# QQ密码
# qq_password = "123"
#
# print('QQ账号：' + qq_number + '\nQQ密码：' + qq_password)


# age = int(input('请输入年龄:'))
# # if语句
# if age >= 18:
#     print("可以去网吧happy")
# else:
#     print("未成年")

# 石头剪刀布
# 玩家
# player = int(input("请输入您要出的拳 石头（1）/ 剪刀（2）/ 布（3）:"))
# 电脑
# computer = randint(1, 3)
# print('玩家选择的拳头是 %d / 电脑出的拳头是 %d' % (player, computer))
# if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
#     print('玩家胜利')
# elif player == computer:
#     print('平局')
# else:
#     print('电脑胜利')
# result = 0
# i = 0
# while i <= 100:
#     if i % 2 == 0:
#         # print(i)
#         result += i
#     i = i + 1
#
# print(result)

# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1
# 九九乘法表
# row = 9
# while row >= 1:
#     col = 1
#     while col <= row:
#         # print(col)
#         print('%d*%d=%d \t' % (col, row, row * col), end="")
#         col += 1
#     print('')
#     row -= 1
# print('------------------------------------------------------------------------')
# for i in range(1, 10):
#     # print(i)
#     for j in range(1, i + 1):
#         print('%d*%d=%d \t' % (j, i, i * j), end="")
#     print('')
name = ['zhangsan', 'lisi', 'wangwu']
print(name)
# 获取个数
print('个数：', len(name))
# 获取每个位置的元素
print('获取索引为0的元素：', name[0])
# 追加元素
name.append('wangli')
print('追加元素：', name)
# 把元素添加到指定位置
name.insert(1, 'jack')
print('把元素添加到索引1：', name)
# 删除末尾元素
name.pop()
print('删除末尾元素：', name)
# 删除指定位置元素
name.pop(3)
print('删除索引为3的元素：', name)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print('打印Apple:', L[0][0])
# 打印Python:
print('打印Python:', L[1][1])
# 打印Lisa:
print('打印Lisa:', L[2][2])
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

height = 1.75
weight = 80.5
bmi = weight / (height * height)
print('小明的BMI指数为：', bmi)
if bmi < 18.5:
    print('BMI指数过轻')
elif 25 > bmi >= 18.5:
    print('BMI指数正常')
elif 28 > bmi >= 25:
    print('BMI指数过重')
elif 32 > bmi >= 28:
    print('BMI指数肥胖')
else:
    print('BMI指数严重肥胖')
print('-------------------------------')

passwords = ['123', '234', '345']
for password in passwords:
    print(password)
print('-------------------------------')
# 1到100的整数之和
sam = 0
for x in range(101):
    sam += x
print('1到100的整数和：', sam)
print('-------------------------------')
d = {'jack': 95, 'zhangsan': '70', 'lisi': 100}
print(d['zhangsan'])
print('-------------------------------')

# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

n1 = 255
n2 = 1000
print(str(hex(n1)))
print(str(hex(n2)))
