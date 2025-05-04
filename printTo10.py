def printTo10(n):
    if n > 10:
        return
    print(n)

    printTo10(n+1)



printTo10(1)