from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissor")
root.geometry("200x200")
lbl = Label(text="Your guess: ")
entry = Entry()
lbl2 = Label(text="Computer's guess: ")
text = Text(width = 16, height = 1)


def computerGuess():
    # use rng system to guess
    text.delete(1.0, "end")
    guess = random.randint(1, 3)
    if guess == 1:
        text.insert(END, "Rock")
    if guess == 2:
        text.insert(END, "Paper")
    if guess == 3:
        text.insert(END, "Scissors")

btn = Button(text="Go", width = 6, height = 1, command=computerGuess)

lbl.pack()
entry.pack()
lbl2.pack()
text.pack()
btn.pack()
root.mainloop()