arr = {23, 5, 7, 2, 14, 34, 23, 6}
max = 0
for i in range(1, len(arr)):
    # if max < arr[i]:
    #     max = arr[i]
    if max < arr[i]:
        max = arr[i]
print(max)
