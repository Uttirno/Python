a = int(input())
b = int(input())

def oneiteration():
    iteration = 0
    for i in range(1):
        iteration+= 1

    return a*b

def niteration(n):
    iteration = 0
    for i in range(0, n):
        iteration += 1

    return a*b

print("1 iteration: ", oneiteration())
print("n iterations: ", niteration(30))