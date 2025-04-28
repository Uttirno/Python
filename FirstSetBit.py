n = int(input("Enter Binary Representation"))
nList = []
for i in range(len(str(n))):
    nList.append(str(n)[i])

for i in nList:
    if int(i) == 1:
        print(i)
    break