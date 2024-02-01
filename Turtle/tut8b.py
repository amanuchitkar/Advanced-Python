from turtle import *

t = Turtle()
bgcolor("black")
t.speed(3)
lists = ["purple", "red", "orange", "blue", "green", "yellow"]
for i in range(300):
    t.color(lists[i % 6])
    t.pensize(i / 20 + 1)
    t.forward(i)
    t.left(59)

done()
