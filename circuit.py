def findCircuit(a,b,c):
    part1 = a and b
    part2 = b and c
    part3 = not a and c
    q = part1 or part2 or part3
    return q

print(findCircuit(int(input()), int(input()), int(input())))
