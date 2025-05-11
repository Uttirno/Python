def checkSorted(a):
    length = len(a)
    if length == 1 or length == 0:
        return True

    return a[0] <= a[1] and checkSorted(a[1:])

arr = [1, 2, 3, 4]

if checkSorted(arr):
    print("The array is sorted")
else:
    print("The array is not sorted")