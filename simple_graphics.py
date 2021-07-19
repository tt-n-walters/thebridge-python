import arcade
import random
import math

t = 0
arcade.open_window(1280, 720, "Simple graphics")

def draw(deltatime):
    global t
    arcade.draw_rectangle_filled(1280/2, 720*2/3, 1280, 720*2/3, arcade.color.SKY_BLUE)
    arcade.draw_rectangle_filled(1280/2, 720*1/6, 1280, 720*1/3, arcade.color.GO_GREEN)
    x = 500 + math.sin(t / 20) * 30
    y = 600 + math.cos(t / 10) * 30
    arcade.draw_triangle_filled(x, y, 350, 200, 650, 200, arcade.color.FOREST_GREEN)
    arcade.draw_rectangle_filled(500, 150, 50, 100, arcade.color.DARK_BROWN)

    t = t + 1


arcade.schedule(draw, 1/60)
arcade.run()
