def checkPow(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if(n%4 == 0):
        return checkPow(n/4)
    return False

s = int(input("Enter number"))
if checkPow(s):
    print("s is power of 4")
else:
    print("s is not power of 4")
