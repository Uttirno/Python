from math import sqrt
k = int(input())


def checkIfPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            return False

    return True

for l in range(k+1, 0, -1):
    temp = str(l)
    if len(temp) == 2:
        if checkIfPrime(l):
            print(l)
