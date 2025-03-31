i =  int(input())
j =  int(input())

while j:
    k = j
    j = i % j
    i = k

print(i)