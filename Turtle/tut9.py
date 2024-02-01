from turtle import *

# bgcolor("0, 0, 0")


def ractangle(color):
    t.begin_fill()
    t.fillcolor(color)
    t.forward(300)
    t.right(90)
    t.fd(70)
    t.right(90)
    t.fd(300)
    t.right(90)
    t.fd(70)
    t.right(90)
    t.end_fill()


t = Turtle()
t.up()
t.goto(0, -300)
t.down()
t.goto(0, 300)
ractangle("orange")
t.goto(0, 230)
ractangle("white")
t.goto(0, 160)
ractangle("green")
t.goto(150, 160)
t.color("blue")
t.circle(35)
t.left(90)
t.fd(35)
for i in range(24):
    t.fd(35)
    t.bk(35)
    t.left(15)
t.hideturtle()
done()
