def MaxElementArray(a):
    length = len(a)

    if length == 1:
        return a[0]

    return max(a[0], MaxElementArray(a[1:]))

arr = [1, 4, 6, 1000, 120, 2]
print(MaxElementArray(arr))