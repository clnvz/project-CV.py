from turtle import Screen
from snake import Snake
from food import Food
import time

WINDOW_SIZE = 300
SNAKE_SPEED = 0.1

border = Screen()
border.setup(height=WINDOW_SIZE * 2, width=WINDOW_SIZE * 2)
border.bgcolor("black")
border.title("Elongate my python :3")
border.tracer(0)

snake = Snake(WINDOW_SIZE)
food = Food(WINDOW_SIZE)
started = True
while started:
    if snake.head.distance(food) < 15:
        snake.longer_snake()
        while snake.food_overlap(food):
            food.relocate(WINDOW_SIZE)

    if snake.game_rules(WINDOW_SIZE):
        started = snake.game_over()

    border.listen()
    border.onkey(key="Up", fun=snake.upwards)
    border.onkey(key="Left", fun=snake.left_turn)
    border.onkey(key="Down", fun=snake.downwards)
    border.onkey(key="Right", fun=snake.right_turn)

    border.update()
    time.sleep(SNAKE_SPEED)
    snake.move_forward()
border.exitonclick()
