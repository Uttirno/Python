def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)

s = int(input("Enter your Number: "))
print(f"factorial of {s} is {factorial(s)}")