import math

def PowerSet(set, setSize):
    PowerSize = (int) (math.pow(2, setSize))
    outer = 0
    inner = 0

    for outer in range(0, PowerSize):
        for inner in range(0, setSize):
            if((outer & (1 << inner))> 0):
                print(set[inner], end=' ')
        print(' ')

size = int(input("Enter Size: "))

set = []

for i in range(size):
    n = int(input("Enter your number here: "))
    set.append(n)

PowerSet(set, len(set))