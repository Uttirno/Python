number = int(input("Enter your number here: "))
digits = len(str(number))
result = 0
temp = number


while temp > 0:
    digit = temp % 10
    result += digit ** digits
    temp//=10

if number == result:
    print("your number is a armstorng number")
else:
    print("your number is not a armstrong numebr")