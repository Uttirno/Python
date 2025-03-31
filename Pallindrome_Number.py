number = int(input("Enter your number here: "))
reverse = 0
og = number

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print(og == int(reverse))
