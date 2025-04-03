def isEvenOdd(number):
    if number ^ 1 == number+1:
        return True
    else:
        return False

number = int(input())

if isEvenOdd(number):
    print("This is a even number")
else:
    print("This is a odd number")