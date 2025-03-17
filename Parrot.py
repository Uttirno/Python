class Parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

bob = Parrot("Bob", "4")

william = Parrot("William", 5)

print(bob.name, " is a", bob.species)
print(william.name, " is a", william.species)

print(bob.name, " is", bob.age, " years old")
print(william.name, " is", william.age, " years old")