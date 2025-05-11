def arrayLen(a):
    if a == []:
        return 0

    return 1 + arrayLen(a[1:])

arr = [1, 2, 3]

print("The length of the array is ", arrayLen(arr))