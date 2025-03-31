def myfunction1(n):
    iteration = 0
    if n <= 0:
        return
    for i in range (0, n+1):
        iteration += 1
        myfunction1(n//2)
        myfunction1(n//3)
    print("With n iterations, time coplexity is:", iteration)

myfunction1(int(3))