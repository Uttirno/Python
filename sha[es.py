import turtle
t = turtle.Turtle()
s = turtle.Screen()
t.speed("fastest")
t.width(3)

for i in range(3):
    t.forward(100)
    t.left(120)

t.penup()
t.forward(150)

t.pendown()
for i in range(4):
    t.forward(100)
    t.left(90)
    i = i+1

t.penup()
t.forward(150)
t.pendown()
for i in range(8):
    t.forward(50)
    t.left(45)
    
