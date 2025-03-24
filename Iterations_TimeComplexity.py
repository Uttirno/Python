def abc(n):
    return n + n+2 / 2 * n**n + n-7
def abcd(n):
    sum = 0
    for i in range(n, n+1):
        sum+= 1

    return sum
def abcde(n):
    sum = 0
    for i in range(n, n*3):
        for i in range(n, n*n+3):
            sum+= 1
    return sum
print(abc(4))
print(abcd(4))
print(abcde(4))