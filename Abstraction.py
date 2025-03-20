class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat, my name is {self.name} and i am {self.age} years old")

    def makesound(self):
        print('Meow')

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog, my name is {self.name} and i am {self.age} years old")

    def makesound(self):
        print('bark')

cat1 = Cat("cat", 3)
dog1 = Dog("Tom", 7)

for animal in cat1, dog1:
    animal.info()
    animal.makesound()