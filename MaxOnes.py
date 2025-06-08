def getMaxOnes(a, a_size):
    counter = 0
    maxones = 0
    for i in range(0, a_size):
        if (a[i] != 0):
            counter += 1
            maxones = max(maxones, counter)
    return maxones
a = [1, 0, 1, 0, 1, 1]
a_size = len(a)
result = getMaxOnes(a, a_size)
print(f"Max Ones: {result}")
