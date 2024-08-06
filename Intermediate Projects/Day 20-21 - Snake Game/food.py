from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, size):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.relocate(size)

    def relocate(self, size):
        self.setx(random.randrange(-size + 40, size - 40, step=20))
        self.sety(random.randrange(-size + 40, size - 40, step=20))
