def check(num):
    return num > 0 and (num & (num - 1)) == 0 and (n.bit_length() - 1) % 3 == 0

n = int(input("Enter your number here: "))
i = check(n)
print(i)