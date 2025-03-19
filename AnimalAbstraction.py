

class Animal():

    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run!")

class Snake(Animal):
    def move(self):
        print("I can crawl.")

class Fish(Animal):
    def move(self):
        print("I can swim!")


x, y, z = Human(), Snake(), Fish()
x.move()
y.move()
z.move()