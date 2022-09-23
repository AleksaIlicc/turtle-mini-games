from turtle import Screen,Turtle
screen=Screen()
t=Turtle()

def movef():
    t.forward(20)
def moveb():
    t.back(20)
def clear():
    t.clear()
    t.penup()
    t.setposition(0,0)
    t.pendown()
    t.setheading(0)
def directionl():
    t.left(10)
def directionr():
    t.right(10 )


screen.listen()
screen.onkey(clear,"c")
screen.onkey(movef,"Up")
screen.onkey(moveb,"Down")
screen.onkey(directionl,"Left")
screen.onkey(directionr,"Right")

screen.exitonclick()