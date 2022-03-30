from turtle import Turtle, Screen

cute_turtle = Turtle()
screen = Screen()


def move_forward():
    cute_turtle.forward(20)


def move_backward():
    cute_turtle.back(20)


def turn_left():
    cute_turtle.left(10)


def turn_right():
    cute_turtle.right(10)


def clear_screen():
    cute_turtle.reset()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "space")
screen.exitonclick()
