def fibonacci(t):
    a = 0
    b = 1

    if t == 1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2, t):
            c = a + b
            a = b
            b = c
            print(c)

n = int(input("Enter A Number: "))
fibonacci(n)
