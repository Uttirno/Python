def ways(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1

    twoStep = 0
    oneStep = 0

    if (stairs >= 2):
        twoStep = ways(stairs - 2)

    oneStep =  ways(stairs - 1)
    return twoStep + oneStep

print(ways((int)input("Enter number of stairs")))