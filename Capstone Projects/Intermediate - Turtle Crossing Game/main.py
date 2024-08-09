from turtle import Screen
from player import Player
from vehicles import Car, SuperCar
from master import GameMaster
import time

window_size = 600
max_speed = 0.01

window = Screen()
window.title("Turtle Crossing Game by clnvz.py")
window.colormode(255)
window.setup(height=window_size, width=window_size)
player_color = window.textinput(title="Choose a color", prompt="red/orange/yellow/green/blue/purple").lower()
window.tracer(0)

player = Player(window_size, player_color)
game_master = GameMaster()

cars = []
supercars = []


def add_car(num):
    for _ in range(num):
        new_car = Car()
        cars.append(new_car)


def add_supercar():
    new_car = SuperCar()
    supercars.append(new_car)


def end_game():
    for veh in cars:
        veh.hideturtle()
    for veh in supercars:
        veh.hideturtle()


add_car(15)

vehicle_speed = 0.2
game_is_on = True
while game_is_on:
    time.sleep(vehicle_speed)
# INCREASE DIFFICULTY
    if player.ycor() >= 270:
        vehicle_speed *= 0.7
        player.refresh()
        game_master.increase_level()
        if game_master.level == 3 or game_master.level == 5 or game_master.level == 9:
            add_supercar()
        elif game_master.level < 7:
            add_car(2)
# IF PLAYER-VEHICLE COLLISION OCCURS
    for vehicle in cars:
        if player.distance(vehicle) < 30 and player.ycor() - 10 < vehicle.ycor():
            end_game()
            player.game_over()
            game_master.game_over()
            game_is_on = False
    for vehicle in supercars:
        if player.distance(vehicle) < 30 and player.ycor() - 10 < vehicle.ycor():
            end_game()
            player.game_over()
            game_master.game_over()
            game_is_on = False

    window.listen()
    window.onkeypress(player.upwards, "Up")

    for car in cars:
        car.move_vehicle()
    for supercar in supercars:
        supercar.move_supercar()
    window.update()

window.exitonclick()
