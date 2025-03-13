import turtle

turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Square")

board = turtle.Turtle()
board.width(4)

for i in range(4):
    board.forward(100)
    board.left(90)
    i = i + 1
