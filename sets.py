set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {4, 5, 6, 7}
print("Set1:",set1)
print("Set2", set2)

# Additon

set1.add("1234567890")
set2.add("abcd")
print(f"{set1}, {set2}")

# Difference

print(set1.difference(set2))
print(set1.symmetric_difference(set2))
