def factorial(i):
    if i == 1:
        return i
    else:
        return i * factorial(i-1)

n = int(input("Enter a Number"))
if n > 0:
    print(factorial(n))
else:
    print("Negetive numbers are not allowed")
    

