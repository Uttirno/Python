def tailrec(n, num):
    if n > num:
        return
    print(n)
    tailrec(n + 1, num)


tailrec(1, 10)