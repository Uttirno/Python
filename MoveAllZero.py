def moveAllZero(a):
    a.sort()
    return a[::-1]
    
a = [1,2,3, 40223, 43, 534, 1292384, 0, 0, 0, 21234, 8137, 921, 0, 49234]

result = moveAllZero(a)
print(result)
