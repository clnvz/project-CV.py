from turtle import Turtle

DISPLACEMENT = 20
STARTING = (0, 0), (-20, 0), (-40, 0)
SCORE_ALIGNMENT = "center"
SCORE_FONT = ("Courier", 15, "normal")


class Snake:
    snake_body = []

    def __init__(self, size):
        for position in STARTING:  # STARTING SNAKE
            self.extend_snake(position)
        self.head = self.snake_body[0]

        self.score = 0  # SCOREBOARD
        self.scorer = Turtle()  # SCORER
        self.scorer.color("white")
        self.scorer.penup()
        self.scorer.hideturtle()
        self.scorer.goto(0, size - 20)
        self.update_score()

    def extend_snake(self, position):
        snake = Turtle(shape="square")
        snake.color("blue")
        snake.penup()
        snake.speed(0)
        snake.goto(position)
        self.snake_body.append(snake)

    def longer_snake(self):
        tail = self.snake_body[-1].pos()
        self.extend_snake(tail)
        self.score += 1
        self.update_score()

    def update_score(self):
        self.scorer.clear()
        self.scorer.write(arg=f"Current score: {self.score}", align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def move_forward(self):
        for seg in range(len(self.snake_body) - 1, 0, -1):
            front_x = self.snake_body[seg - 1].xcor()
            front_y = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(x=front_x, y=front_y)
        self.snake_body[0].forward(DISPLACEMENT)

    def upwards(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def downwards(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left_turn(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right_turn(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def food_overlap(self, food):
        for seg in self.snake_body:
            if seg.distance(food) < 15:
                return True
        return False

    def game_rules(self, size):
        for body in self.snake_body[1:]:
            if self.head.distance(body) < 15:
                return True
        if (self.head.xcor() >= size or self.head.xcor() <= -size
                or self.head.ycor() >= size or self.head.ycor() <= -size):
            return True

    def game_over(self):
        self.scorer.clear()
        game_over = Turtle()
        game_over.color("white")
        game_over.hideturtle()
        game_over.write(arg=f"laaahh :(\nFinal score: {self.score}",
                        align=SCORE_ALIGNMENT, font=SCORE_FONT)
        return False
