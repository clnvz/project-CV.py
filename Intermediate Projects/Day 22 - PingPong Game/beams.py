from turtle import Turtle

ARENA_HEIGHT = 700
ARENA_WIDTH = 1100
#############################
RIGHT_SIDE = ARENA_WIDTH / 2
LEFT_SIDE = -RIGHT_SIDE
HOME_RIGHT = RIGHT_SIDE - 20
HOME_LEFT = LEFT_SIDE + 20
DISPLACEMENT = 50


class Beam(Turtle):

    def __init__(self, position, length):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=length, stretch_len=1)
        self.speed(0)
        self.color("white")
        self.goto(position)

    def upwards(self):
        if self.ycor() < ((ARENA_HEIGHT / 2) - 90):
            new_y = self.ycor() + DISPLACEMENT
            self.goto(x=self.xcor(), y=new_y)

    def downwards(self):
        if self.ycor() > ((-ARENA_HEIGHT / 2) + 90):
            new_y = self.ycor() - DISPLACEMENT
            self.goto(x=self.xcor(), y=new_y)

    def refresh(self, side):
        self.goto(x=side, y=0)
        self.goto(x=side, y=0)
