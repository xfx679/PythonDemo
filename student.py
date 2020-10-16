class Student(object):
    def __init__(self, name, score):
        # 加下划线代表为私有的变量（private）
        self._name = name
        self._score = score

    # 当变量为私有变量时，得增加get方法
    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    # 允许外部修改，增加set方法
    def set_name(self):
        return self._name

    def set_score(self):
        return self._score



bate = Student('12312', 12)
print(bate.get_name(), bate.get_score())
