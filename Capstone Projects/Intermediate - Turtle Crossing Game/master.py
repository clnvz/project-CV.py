from turtle import Turtle

NAME_FONT = ("Courier", 17, "bold")
FINAL_FONT = ("Courier", 20, "bold")

FINISH_LINE = 20


class GameMaster(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.width(5)
        self.write_lines()

        self.level = 0
        self.increase_level()

    def write_lines(self):
        self.goto(300, 250)
        self.seth(180)
        while self.xcor() > -300:
            self.forward(FINISH_LINE)
            self.pendown()
            self.forward(FINISH_LINE)
            self.penup()
        self. goto(300, -240)
        self.seth(180)
        while self.xcor() > -300:
            self.forward(FINISH_LINE)
            self.pendown()
            self.forward(FINISH_LINE)
            self.penup()

    def increase_level(self):
        self.clear()
        self.write_lines()
        self.level += 1
        self.goto(-290, 270)
        self.write(arg=f"Level: {self.level}", align="left", font=NAME_FONT)

    def game_over(self):
        self.clear()
        self.home()
        self.write(arg="Game Over\n\n", align="center", font=FINAL_FONT)
        self.write(arg=f"You made it until level {self.level}.", align="center", font=FINAL_FONT)
