n = ["apple", "orange", "grapes", 1, 2, 3, True, False]

print("List: ", n)

n.append("guava")

print("Updated list: ", n)

n.remove("grapes")

print("Updated List", n)

n.sort()

print("Sorted List: ", n)

n.pop(1)

print("Updated list: ", n)

n.reverse()
print("Reversed List: ", n)

n = n[:4]

print("Sorted List: ", n)

n.clear()

print("Updated List: ", n")