import turtle

tv = turtle.Screen()

jarvis = turtle.Turtle()
jarvis.shape('turtle')
jarvis.color('green')

friday = turtle.Turtle()
friday.shape('turtle')
friday.color('blue')

count = 0
while count < 50:
    jarvis.forward(200)
    jarvis.left(80+count)
    jarvis.forward(200)
    jarvis.left(80+count)
    friday.backward(200)
    friday.right(80+count)
    friday.backward(200)
    friday.right(80+count)
    count += 1


tv.exitonclick()