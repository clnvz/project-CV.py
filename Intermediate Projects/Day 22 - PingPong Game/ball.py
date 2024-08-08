from turtle import Turtle

ARENA_HEIGHT = 700
#############################
TOP_WALL = (ARENA_HEIGHT / 2) - 20
BOTTOM_WALL = (-ARENA_HEIGHT / 2) + 20


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("yellow")
        self.speed(0)
        self.x_displace = 10
        self.y_displace = 10
        self.refresh()

    def refresh(self):
        self.home()

    def move(self):
        self.goto(self.xcor() + self.x_displace, self.ycor() + self.y_displace)

    def bounce_wall(self):
        if self.ycor() >= TOP_WALL or self.ycor() <= BOTTOM_WALL:
            self.y_displace *= -1

    def bounce_beam(self):
        self.x_displace *= -1
