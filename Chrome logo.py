from turtle import Turtle,Screen
turtle = Turtle()
screen = Screen()

turtle.circle(70)
turtle.right(90)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.left(90)
turtle.circle(90)
turtle.right(90)
turtle.penup()
turtle.forward(200)
turtle.left(90)
turtle.pendown()
turtle.circle(290)
turtle.penup()
turtle.left(90)
turtle.forward(379)
turtle.pendown()
turtle.right(90)
turtle.forward(276)
turtle.back(276)
turtle.penup()
for _ in range(2) :
    for _ in range(120) :
        turtle.forward(1.55825)
        turtle.right(1)
    turtle.pendown()
    turtle.forward(276.5)
    turtle.back(276.5)
    turtle.penup()

screen.mainloop()