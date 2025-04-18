def powerOf2(number):
    if number == 0:
        return 0
    if ((number & (~(number - 1)))== number):
        return 1
    return 0


if powerOf2(int(input("Enter your number here"))):
    print("The number is power of 2")
else:
    print("The number is not power of 2")