from turtle import Turtle

DISPLACEMENT = 20


class Player(Turtle):

    def __init__(self, size, player_color):
        super().__init__()
        self.edge = size / 2
        self.shape("turtle")
        self.color(player_color)
        self.penup()
        self.seth(90)

        self.x_coor = 0
        self.y_coor = -self.edge + 40
        self.move_player()

    def refresh(self):
        self.x_coor = 0
        self.y_coor = -self.edge + 40
        self.move_player()

    def move_player(self):
        self.goto(self.x_coor, self.y_coor)

    def upwards(self):
        if self.ycor() < self.edge - 20:
            self.y_coor += DISPLACEMENT
            self.move_player()

    def game_over(self):
        self.hideturtle()

    # def downwards(self):
    #     if self.ycor() > -self.edge + 40:
    #         self.y_coor -= DISPLACEMENT
    #         self.move_player()

    # def to_left(self):
    #     if self.xcor() > -self.edge + 20:
    #         self.x_coor -= DISPLACEMENT
    #         self.move_player()

    # def to_right(self):
    #     if self.xcor() < self.edge - 20:
    #         self.x_coor += DISPLACEMENT
    #         self.move_player()
