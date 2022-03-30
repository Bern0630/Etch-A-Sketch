import random
import turtle
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which user will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
is_user_bet_true = False

while not is_user_bet_true:
    if user_bet in colors:
        is_race_on = True
        is_user_bet_true = True
        y_pos = [-100, -60, -20, 20, 60, 100]
        all_turtles = []
        for index in range(0, 6):
            cute_turtle = Turtle(shape="turtle")
            cute_turtle.color(colors[index])
            cute_turtle.penup()
            cute_turtle.goto(x=-230, y=y_pos[index])
            all_turtles.append(cute_turtle)
    elif user_bet == "bye":
        is_race_on = False
        is_user_bet_true = True
        print("thanks for joining!")
    else:
        user_bet = screen.textinput(title="make your bet", prompt="which user will win the race?")

while is_race_on:
    for i in all_turtles:
        move_forward = random.randint(0, 10)
        i.forward(move_forward)
        if i.xcor() > 220:
            is_race_on = False
            if user_bet == i.pencolor():
                print(f"you've won! the {i.pencolor()} is the winner!")
                break
            else:
                print(f"you've lost! the {i.pencolor()} is the winner!")
                break
screen.exitonclick()




