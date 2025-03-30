def binaryToDecimal(binary):
    dec, i = 0, 0

    while binary != 0:
        j = binary % 10
        dec = dec + j * 2 ** i
        binary = binary // 10
        i += 1

    print(dec)
try:
    binaryToDecimal(int(input("Enter your number here: ")))
except:
    exit(code="There is an error in your input.")
