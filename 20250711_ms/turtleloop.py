import turtle

tv = turtle.Screen()

mypet = turtle.Turtle()
mypet.shape('turtle')
mypet.speed(200)
mypet.color('blue')

ranga = ['blue' , 'green' , 'orange' , 'red' ,'yellow' ]
count = 0
for i in range(1000):
    mypet.forward(100)
    mypet.left(90+i)
    mypet.forward(50)
    mypet.left(90+i)
    mypet.forward(100)
    mypet.right(90+i)
    mypet.backward(50)
    mypet.right(180+i)
    if i == 600:
        count = 0
        
    if i == 100 or i == 600:
        mypet.color(ranga[count]) 
        count += 1
    elif i == 200 or i == 700:
        mypet.color(ranga[count] )
        count += 1
    elif i == 300 or i == 800:
        mypet.color(ranga[count] )
        count += 1
    elif i == 400 or i == 900:
        mypet.color(ranga[count] )
        count += 1
    elif i == 500:
        mypet.color(ranga[count] )
        count += 1
    else:
        print(i , count)

tv.exitonclick()