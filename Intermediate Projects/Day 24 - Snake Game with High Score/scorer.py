from turtle import Turtle

SCORE_ALIGNMENT = "center"
SCORE_FONT = ("Courier", 15, "normal")


class Scorer(Turtle):

    def __init__(self, size):
        super().__init__()
        self.score = 0  # SCOREBOARD
        with open("data.txt") as highest:
            self.highest_score = int(highest.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, size - 20)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Current score: {self.score} Highest score: {self.highest_score}",
                   align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def add_point(self):
        self.score += 1
        self.update_score()

    def refresh(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as highest:
                highest.write(str(self.highest_score))
        self.score = 0
        self.update_score()
