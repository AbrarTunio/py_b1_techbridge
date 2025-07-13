# pip install turtles

import turtle

scr = turtle.Screen()

jony = turtle.Turtle()
jony.shape('turtle')
jony.color('green')

jony.speed(100)
jony.forward(200)

jony.left(90)
jony.forward(200)

jony.left(90)
jony.forward(200)

jony.left(90)
jony.forward(200)

jony.color('red')
jony.right(90)
jony.forward(100)

jony.right(90)
jony.forward(200)

jony.right(90)
jony.forward(100)

jony.left(135)
jony.forward(65)

jony.left(85)
jony.forward(65)
jony.backward(65)

jony.left(180-40)
jony.forward(225)

jony.right(65)
jony.forward(50)

scr.exitonclick()