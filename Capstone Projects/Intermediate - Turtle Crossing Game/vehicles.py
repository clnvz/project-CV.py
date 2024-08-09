from turtle import Turtle
import random

CAR_LENGTH = 2
DISPLACEMENT = 10
STARTING_X = []
for x in range(-330, 320):
    STARTING_X.append(x)
STARTING_Y = []
for y in range(-220, 240, 20):
    STARTING_Y.append(y)


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.seth(180)
        self.color(((random.randint(0, 250)), (random.randint(0, 255)), (random.randint(0, 255))))
        self.shapesize(stretch_wid=1, stretch_len=CAR_LENGTH)
        self.goto(random.choice(STARTING_X), random.choice(STARTING_Y))

    def move_vehicle(self):
        if self.xcor() < -330:
            self.respawn()
        self.forward(DISPLACEMENT)

    def respawn(self):
        self.goto(320, random.choice(STARTING_Y))


class SuperCar(Car):

    def __init__(self):
        super().__init__()
        self.color("red")

    def move_supercar(self):
        if self.xcor() < -330:
            self.respawn()
        self.forward(DISPLACEMENT + 15)
