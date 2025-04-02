from math import sqrt

j = int(input("Enter your number here: "))

def checkIfPrime(number):
    if number > 1:
        for i in range(2, int(sqrt(number))+1):
            if number % i == 0:
                return False
                break
        else:
            return True
    else:
        exit(code="Your number is incorrect")

if checkIfPrime(j):
    print("This is a prime number")
else:
    print("This is not a prime number")