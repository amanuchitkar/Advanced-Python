from turtle import *

t = Turtle()


def circale(a, b, c, d):
    t.up()
    t.goto(a, b)
    t.down()
    t.begin_fill()
    t.fillcolor(d)
    t.circle(c)
    t.end_fill()
    t.up()
    t.home()
    t.down()


circale(0, -50, 50, "green")
circale(200, 200, 50, "orange")
circale(-200, 200, 50, "blue")
circale(-200, -200, -50, "red")
circale(200, -200, -50, "yellow")
done()
