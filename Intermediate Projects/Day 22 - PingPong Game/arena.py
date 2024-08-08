from turtle import Turtle

ARENA_HEIGHT = 700
ARENA_WIDTH = 1100
WINNING_SCORE = 5
#############################
RIGHT_SIDE = ARENA_WIDTH / 2
LEFT_SIDE = -RIGHT_SIDE
NAME_FONT = ("Courier", 27, "normal")
SCORE_FONT = ("Courier", 31, "bold")
FINAL_FONT = ("Courier", 20, "normal")


class Arena(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.speed(0)
        self.hideturtle()

    def display_net(self):
        self.width(5)
        self.hideturtle()
        self.goto(0, -700)
        self.seth(90)
        while self.ycor() < 700:
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()

    def display_name(self, name_left, name_right):
        self.penup()
        self.goto(0, 300)
        self.write(arg="P I N G   P O N G", align="center", font=NAME_FONT)
        self.goto(-520, 300)
        self.write(arg=name_left, align="left", font=NAME_FONT)
        self.goto(520, 300)
        self.write(arg=name_right, align="right", font=NAME_FONT)

    def scoreboard(self, ballx):
        self.clear()
        if ballx < LEFT_SIDE and ballx != 0:
            self.right_score += 1
        elif ballx > RIGHT_SIDE and ballx != 0:
            self.left_score += 1
        self.write_score()

    def write_score(self):
        if self.left_score == WINNING_SCORE or self.right_score == WINNING_SCORE:
            return False
        else:
            self.goto(-275, 175)
            self.write(arg=self.left_score, align="center", font=SCORE_FONT)
            self.goto(275, 175)
            self.write(arg=self.right_score, align="center", font=SCORE_FONT)
            return True

    def game_winner(self, name_left, name_right):
        self.clear()
        self.home()
        self.write(arg=f"GAME OVER!\n\n{name_left} - {self.left_score}pts\n"
                       f"{name_right} - {self.right_score}pts\n", align="center", font=FINAL_FONT)
        self.goto(0, -60)
        if self.left_score > self.right_score:
            self.write(arg=f"{name_left} wins!", align="center", font=FINAL_FONT)
        else:
            self.write(arg=f"{name_right} wins!", align="center", font=FINAL_FONT)
