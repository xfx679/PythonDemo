def callback(input):
    array = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1,
             0, 0, 1, 1, 4, 5, 2, 3, 4, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0]

    print(len(array))
    s = ''
    for i in range(len(array)):
        # print(i)
        if i % 7 == 0:
            s += '\n'
        if array[i] == 0:
            s += "   "
        elif array[i] == 4:
            s += "  "
        elif array[i] == 5:
            s += " I "
        elif array[i] == 2:
            s += "Love "
        elif array[i] == 3:
            s += "You"
        else:
            s += "  " + input
    return s


print(callback('*'))

# array = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1,
#          0, 0, 1, 1, 4, 5, 2, 3, 4, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
#          0, 0, 0, 0, 0, 0]
#
# lenght = len(array)
# for a in range(len(array)):
#     if a % 7 == 0:
#         print('#')
