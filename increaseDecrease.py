def incDec(n, num):
    if((n < 0 ) or (n > num)):
        return
    print(n)
    incDec(n - 1, num)
    print(n)

incDec(10, 10)