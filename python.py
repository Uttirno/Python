def abc(n):
    iteration = 0
    for i in range(0, n):
        for j in range(0, n):
            print("*", end=" ")
            iteration += 1

        print(" ")

    print("When n is ", n, " iterations = ", iteration)

abc(2)
abc(3)
abc(8)