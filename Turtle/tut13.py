from turtle import *

t = Turtle()

bgcolor("black")
t.speed(0)
t.pensize(2)
lists = ["red", "blue", "green", "white", "yellow", "magenta"]
# while True:
for i in range(6):
    for colors in lists:
        t.color(colors)
        t.circle(100)
        t.left(10)
        # t.right(15)
t.hideturtle()
done()
