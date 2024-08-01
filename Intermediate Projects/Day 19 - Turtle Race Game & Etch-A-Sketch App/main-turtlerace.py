from turtle import Turtle, Screen
import random

arena = Screen()
arena.screensize(500, 400)
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coor = [-125, -75, -25, 25, 75, 125]
racers = []
player_color = arena.textinput("Which turtle color will win the race?",
                               "Pick from either red/orange/yellow/green/blue/purple").lower()
print(f"You placed a bet on: {player_color.title()} turtle")
for num in range(0, 6):
    com_num = Turtle(shape="turtle")
    com_num.color(turtle_colors[num])
    com_num.penup()
    com_num.goto(-380, y_coor[num])
    racers.append(com_num)

start_race = True
while start_race:
    for racer in racers:
        if racer.xcor() > 380:
            start_race = False
            if racer.pencolor() == player_color:
                print(f"{racer.pencolor().title()} turtle finished first. Yay, you win!")
            else:
                print(f"{racer.pencolor().title()} turtle finished first. Sad boy, you lose.")
        racer.forward(random.randint(0, 10))

arena.exitonclick()
