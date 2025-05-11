def arrTotalSum(a):
    length = len(a)

    if length == 1:
        return a[0]

    return a[0] + arrTotalSum(a[1:])

a = [1, 2, 3]

print("Sum or array a is", arrTotalSum(a))