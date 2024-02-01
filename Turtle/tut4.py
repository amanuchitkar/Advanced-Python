from turtle import *

t = Turtle()
n = 0
t.color("red")
t.speed(6)
t.begin_fill()
t.fillcolor()
for i in range(4):
    t.fd(100)
    t.left(90)
t.end_fill()
t1 = Screen()
t1.bgcolor("black")
t.hideturtle()
done()
