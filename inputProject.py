def inputTillNegetive(n):
    if n < 0:
        print("Negative number found: ", n)
        return
    else:
        print("Entered input N: ", n)
        n = int(input())
        inputTillNegetive(n)
ni = int(input())
inputTillNegetive(ni)