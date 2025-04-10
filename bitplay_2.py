def nthNumberSet(number, n):
    if number & (1 << n - 1):
        print('SET')
    else:
        print('NOT SET')


nthNumberSet(int(input()), int(input()))
