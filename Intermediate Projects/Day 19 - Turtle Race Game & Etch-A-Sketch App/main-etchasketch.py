from turtle import Turtle, Screen

canvass = Screen()
pencil = Turtle()


def move_forward():
    pencil.forward(10)


def move_backwards():
    pencil.forward(-10)


def turn_clockwise():
    pencil.right(10)


def turn_cclockwise():
    pencil.left(10)


def clear_canvass():
    pencil.penup()
    pencil.clear()
    pencil.home()
    pencil.pendown()


canvass.listen()
canvass.onkey(key="w", fun=move_forward)
canvass.onkey(key="s", fun=move_backwards)
canvass.onkey(key="d", fun=turn_clockwise)
canvass.onkey(key="a", fun=turn_cclockwise)
canvass.onkey(key="c", fun=clear_canvass)


canvass.exitonclick()
