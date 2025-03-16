set1 = {'green', 'blue'}
set2 = {'yellow', 'blue'}

for i in set1:
    for j in set2:
        if i == j:
            print("Common item found:",i)