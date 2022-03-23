from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
"""
Control : W - forwards, S - backwards, A - turn left, D - turn right, C - clear screen
"""

screen.title("Welcome to the Etch-a-Sketch!")


def change_colour():
    colour = screen.textinput("Choose your colour", "What could would you like?")
    turtle.color(colour)
    screen.listen()


def move_forwards():
    turtle.fd(10)


def move_backwards():
    turtle.back(10)


def turn_left():
    turtle.left(10)


def turn_right():
    turtle.right(10)


def clear_screen():
    screen.resetscreen()


screen.onkeypress(fun=move_forwards, key="w")
screen.onkeypress(fun=move_backwards, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkeypress(fun=clear_screen, key="c")
screen.onkey(fun=change_colour, key="space")

screen.listen()

screen.exitonclick()
