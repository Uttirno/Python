def reverseString(a):
    if len(a) == 1:
        return a[0]

    firstChar = a[0]
    return reverseString(a[1:]) + firstChar

s = "ABC"
print(reverseString(s))
