def NumberOfBits(n):

    count = 0

    while(n):
        n >>= 1
        count += 1

    return count

print(NumberOfBits(int(input())))

