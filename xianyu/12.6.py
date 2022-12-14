# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 12.6.py
@Author : wenjing
@Date : 2022/12/6 17:53
"""
from graphics import *
import random

win = GraphWin('Animation', 600, 600)
circles = []
dx = random.randint(-15, 15)
dy = random.randint(-15, 15)


class Animated_Circle():
    def __init__(self, dx, dy):
        for i in range(5):
            self.c = Circle(Point(300, 300), random.randint(5, 45))
            self.c.setFill(color_rgb(random.randint(0, 255),
                                     random.randint(0, 255),
                                     random.randint(0, 255)))
            self.dx = dx
            self.dy = dy

            circles.append([c, dx, dy])
            self.c.draw(win)
            win.getMouse()

    def outside_x(self):
        center = circles[0].getCenter()
        radius = circles[0].getRadius()
        self.dx = random.randint(-15, 15)
        if self.dx + radius >= 600 or self.dx - radius <= 0:
            return True
        else:
            return False

    def outside_y(self):
        center = circles[0].getCenter()
        radius = circles[0].getRadius()
        self.dy = random.randint(-15, 15)
        if self.dy + radius >= 600 or self.dy - radius <= 0:
            return True
        else:
            return False

    def move(self):
        circles[i][0].move(dx, dy)
        update(30)


circles = []

for i in range(50):
    circles.append(Animated_Circle())

while True:
    for i in range(50):
        circles[i].move()
    update(30)