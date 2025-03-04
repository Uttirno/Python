name = input("Enter your name")
age = input("Enter your age")
weight = input("Enter your weight")

print("Name: ", name)
print("Data type of name: ", type(name))
print("Age ", age)
print("Data type of age: ", type(age))
print("Weight: ", weight)
print("Data type of weight: ", type(weight))

# type casting

print("\n After type casting:")
name = str(name)
age = int(age)
weight = float(weight)

print("Name: ", name)
print("Data type of name: ", type(name))
print("Age ", age)
print("Data type of age: ", type(age))
print("Weight: ", weight)
print("Data type of weight: ", type(weight))
