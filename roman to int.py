def romantoint(n):
    roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "V": 5, "I": 1, "X": 10}

    result = 0

    for i in range(0, len(n) - 1):
        if roman[n[i]] < roman[n[i+1]]:
            result -= roman[n[i]]
        else:
            result = roman[n[i]]


    return result + roman[n[-1]]
r = input()

print(romantoint(r))