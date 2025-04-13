def OddOccuring(arr):
    res = 0
    for element in arr:
        res = res ^ element

    return res

arr = []
n = int(input("Enter array size"))
while n:
    x = int(input("Enter your number:"))
    arr.append(x)
    n-=1

print("odd occuring number is ", OddOccuring(arr))
