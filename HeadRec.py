def headrun(n, num):
    if n > num:
        return
    headrun(n + 1, num)
    print(n)


headrun(1, 10)