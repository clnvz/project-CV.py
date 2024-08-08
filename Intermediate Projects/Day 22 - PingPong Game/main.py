from turtle import Screen
from beams import Beam
from ball import Ball
import time
from arena import Arena

ARENA_HEIGHT = 700
ARENA_WIDTH = 1100
BEAM_LENGTH = 5
#############################
RIGHT_SIDE = ARENA_WIDTH / 2
LEFT_SIDE = -RIGHT_SIDE
HOME_RIGHT = RIGHT_SIDE - 20
HOME_LEFT = LEFT_SIDE + 20

arena = Screen()
arena.bgcolor("black")
arena.setup(width=(RIGHT_SIDE * 2), height=ARENA_HEIGHT)
arena.tracer(0)
arena.title("PINGPONG LACSON!")

left_name = arena.textinput(title="Player 1 (Left side)", prompt="Enter name:").title()
right_name = arena.textinput(title="Player 2 (right side)", prompt="Enter name:").title()
field_maker = Arena()
field_maker.display_name(name_left=left_name, name_right=right_name)
field_maker.display_net()

scorer = Arena()
scorer.scoreboard(0)

left_beam = Beam((HOME_LEFT, 0), BEAM_LENGTH)
right_beam = Beam((HOME_RIGHT, 0), BEAM_LENGTH)
ball = Ball()

arena.update()


def play_game():
    difficulty = 0.03
    game_is_on = True
    while game_is_on:
        time.sleep(difficulty)
        ball.move()
        ball.bounce_wall()

        if ball.xcor() > RIGHT_SIDE or ball.xcor() < LEFT_SIDE:
            scorer.scoreboard(ballx=ball.xcor())
            left_beam.goto(HOME_LEFT, 0)
            right_beam.goto(HOME_RIGHT, 0)
            ball.refresh()
            game_is_on = False

        if not scorer.write_score():
            left_beam.hideturtle()
            right_beam.hideturtle()
            ball.hideturtle()
            field_maker.clear()
            scorer.game_winner(left_name, right_name)

        if (ball.xcor() < HOME_LEFT + 30 and ball.distance(left_beam) < (BEAM_LENGTH * 10)
                or ball.xcor() > HOME_RIGHT - 30 and ball.distance(right_beam) < (BEAM_LENGTH * 10)):
            ball.bounce_beam()
            difficulty -= 0.001

        arena.update()


arena.listen()
arena.onkeypress(key="space", fun=play_game)
arena.onkeypress(key="w", fun=left_beam.upwards)
arena.onkeypress(key="s", fun=left_beam.downwards)
arena.onkeypress(key="Up", fun=right_beam.upwards)
arena.onkeypress(key="Down", fun=right_beam.downwards)

arena.exitonclick()
