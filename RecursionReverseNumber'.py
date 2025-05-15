def reverseNumber(num):
    if num > 0:
        last = num % 10
        if (num // 10 > 0):
            currentNumber = reverseNumber(int(num//10))
            return last * pow(10, len(str(currentNumber))) + currentNumber

        return num

n = int(input("Enter your number"))
print(reverseNumber(n))