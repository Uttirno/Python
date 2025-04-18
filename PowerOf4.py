def powerOf4(number):
    count = 0
    if (number & (~(number & (number - 1)))):
        while number > 1:
            number >>= 1
            count += 1

        if count % 2 == 0:
            return True
        else:
            return False

n = int(input("Enter Your Number here"))
if(powerOf4(n)):
    print("it is power of 4")
else:
    print("it is not  power of 4")