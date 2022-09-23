import turtle
import random
is_game_on = False
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=500, height=400)
userguess = turtle.textinput(
    title="Guess the winner", prompt="Who will win? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

position = -120
for turtle_index in range(6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=position)
    position += 50
    all_turtles.append(new_turtle)
if userguess:
    is_game_on = True
while is_game_on == True:
    for turtle in all_turtles:
        x = turtle.xcor()
        if x > 230:
            is_game_on = False
            winning_color=turtle.pencolor()
            if winning_color==userguess:
                print(f"You've won! The {winning_color} turtle is winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is winner!")

        r_distance=random.randint(1, 8)
        turtle.forward(r_distance)
        
          

screen.exitonclick()
