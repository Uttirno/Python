def sum(n):
    return n*(n+1)/2

def arraysum(a):
    sum = 0
    for i in a:
        sum = sum + i

    return sum

a = [32, 3, 2, 15]

print(arraysum(a))

def sumn(a):
    if a <= 0:
        return
    return n+ sumn(n-1)
