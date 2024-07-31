# # EXTRACTING COLORS FROM IMAGE.JPG
# import colorgram
#
# all_rgb = []
# colors = colorgram.extract('image.jpg', 225)
#
# for num in range(0, len(colors)):
#     r = colors[num].rgb.r
#     g = colors[num].rgb.g
#     b = colors[num].rgb.b
#     all_rgb.append((r, g, b))
#
# print(all_rgb)
#######################################################################
from turtle import Turtle, Screen
import random

canvass = Screen()
painter = Turtle()
painter.shape("arrow")
canvass.colormode(255)
painter.penup()

color_list = [
    (246, 244, 243), (235, 239, 246), (241, 246, 243), (247, 239, 242), (135, 164, 199), (223, 151, 105), (31, 44, 63),
    (200, 137, 148), (160, 61, 51), (235, 212, 93), (49, 100, 139), (138, 181, 162), (147, 64, 72), (56, 49, 47),
    (161, 32, 30), (62, 115, 100), (228, 165, 171), (51, 40, 43), (169, 29, 33), (210, 86, 76), (236, 167, 156),
    (34, 60, 54), (16, 95, 70), (34, 60, 105), (171, 188, 219), (191, 101, 109), (109, 127, 155), (174, 200, 191),
    (36, 149, 206), (20, 83, 104), (64, 66, 57), (157, 201, 221), (101, 141, 131), (131, 128, 121)
]


def hirst_painting(starting_x, starting_y):
    painter.setposition(starting_x, starting_y)
    for _ in range(0, 10):
        for row in range(0, 10):
            painter.dot(20, random.choice(color_list))
            painter.forward(50)
        painter.setx(starting_x)
        painter.seth(90)
        painter.forward(50)
        painter.seth(0)


painter.hideturtle()
hirst_painting(-230, -215) #centers the screen window
canvass.exitonclick()
