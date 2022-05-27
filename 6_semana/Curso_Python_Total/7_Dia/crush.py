#p1
import turtle

turtle.speed(3)
turtle.bgcolor('black')
turtle.pensize(3)

def dibujar():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

    turtle.color('red', 'pink')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(110)
    dibujar()
    turtle.left(120)
    dibujar()
    turtle.forward(110)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.done()

