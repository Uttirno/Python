def numberOfBits(n):
    ones = 0
    zeros = 0

    while(n):
        if n&1 == 1:
            ones+=1
        else:
            zeros+=1


        n >>= 1

    print("Ones = ", ones," Zeros = ", zeros)


numberOfBits(int(input()))
