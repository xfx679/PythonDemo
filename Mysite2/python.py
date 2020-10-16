def getbalancepoint(array):
    num = len(array)
    if num >= 3:
        for i in range(num):
            if i == 0:
                pass
            else:
                list1 = array[:i]  # 将传入的列表切片，将一个列表分成2个列表
                list2 = array[i + 1:]
                sum1 = sum(list1)  # 对切片后的列表分别求和
                sum2 = sum(list2)
                if sum1 == sum2:
                    return '平衡点:%d，其值为%d' % (i, array[i])
        return '无平衡点'
    else:
        return '列表长度不够！'


if __name__ == '__main__':
    print(getbalancepoint([1, 3, 1, 4]))
