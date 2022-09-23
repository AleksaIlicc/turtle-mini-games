import turtle
import random
turtle.colormode(255)
color_list=[(72,209,204),(30,144,255),(138,43,226),(75,0,130),(139,0,139),(186,85,211),(216,191,216),(255,0,255),(218,112,214),(169,169,169),(105,105,105),(230,230,250),(176,196,222),(240,128,128)]
dot=turtle.Turtle()
dot.hideturtle()
dot.speed(10)
screen=dot.getscreen()
screen.screensize(500,500)
i=0
j=0
dim=-350
while i<10:
    dot.penup()
    dot.goto(-350,dim)
    dot.pendown()
    j=0
    while j<10:
        dot.dot(30,random.choice(color_list))
        dot.penup()
        dot.forward(80)
        dot.pendown()
        j+=1
    i+=1
    dim+=80



turtle.exitonclick()