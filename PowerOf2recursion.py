def checkPow(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if(n%2 == 0):
        return checkPow(n/2)
    return False

s = int(input("Enter number"))
if checkPow(s):
    print("is power of 2")
else:
    print("is not power of 2")
