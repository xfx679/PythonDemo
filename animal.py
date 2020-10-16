class Animal(object):

    def run(self):
        print("Animal is running")


class Dog(Animal):
    def run(self):
        print('Dog in running..')

    def eat(self):
        print('Dog eat..')


class Cat(Animal):

    def run(self):
        print('Cat in running..')


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Dog())

# dog = Dog()
# dog.run()
# dog.eat()
#
# cat = Cat()
# cat.run()

a = Animal()
b = Dog()
c = Cat()

# 判断类型
print(isinstance(c, Cat))
print(isinstance(c, Animal))

# 获得对象的所有属性和方法
# print(dir('Animal'))
# 方法长度
print('方法长度', len('Animal'))
