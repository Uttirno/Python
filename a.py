def abc(n):
    looped = True
    itr = 0
    while looped:
        itr += 1
        if itr == n:
            looped = False

    print("when n is ", n, " iteration = ", itr)

abc(70)