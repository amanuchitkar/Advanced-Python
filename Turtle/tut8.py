from turtle import *

t = Turtle()
t.up()
t.goto(200, 0)
lists = ["red", "green", "yellow", "blue"]
for i in lists:
    t.down()
    # t.begin_fill()
    # t.fillcolor(i)
    # t.color("silver")
    t.color(i)
    t.pensize(20)
    t.circle(70)
    # t.end_fill()
    t.up()

    t.backward(100)


done()
