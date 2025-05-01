def FlipBits(number1, number2):

    flips = 0

    while(number1 > 0 or number2 > 0):
        t1 = (number1 & 1)
        t2 = (number2 & 2)
        if(t1 != t2):
            flips += 1

        number1 >>= 1
        number2 >>= 1


    return flips

number1 = int(input("Enter number 1: "))

number2 = int(input("Enter number 2: "))

result = FlipBits(number1, number2)

print(result)