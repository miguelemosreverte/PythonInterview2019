#!/usr/bin/env python
# -*- coding: utf-8 -*-


import string
from collections import namedtuple
from Point.Coordinates.coordinates import lat_lng
from Point.utils.generator import point_generator
from Point.Point import Point




def normalize(points):
    return  [
    Point(
      lat_lng(
        lat = (point.coord.lat/(90*2))+0.5,
        lng = (point.coord.lng/(180*2))+0.5,
        r=2
      ),
      point.timestamp,
      point.extra
    ) for point in points]


def ascii_art(x,y, xx, yy, value = " "):
    # "edge" cases, quite literally!
    left_top = lambda x,y: x == 0 and y == yy
    right_bottom = lambda x,y: x == xx and y == 0
    if left_top(x,y): return " Y ^ "
    if right_bottom(x,y): return " >"
    if y == 0 and x == 0: return " X - "
    if y == 0: return "- "
    if x == 0: return "   |"+ value
    return value

letter =  lambda index: string.ascii_uppercase[index]
class Screen:

    def __init__(self, xx, yy):
        self.xx = xx
        self.yy = yy
        self.screen = [[ascii_art(x,y, xx, yy) for x in range(0,xx+1)]
        for y in range(yy, 0-1, -1)]

    def populate(self, points):
        xx = self.xx
        yy = self.yy
        for index, ((lat, lng, r), timestamp, extra) in enumerate(points):
            x = int(lat * xx)
            y = int(lng * yy)
            self.screen[y][x] = ascii_art(x, yy-y, xx, yy, letter(index))

    def render(self):
        for t in self.screen:
            print(' '.join(t))

class PointList:
    def __init__(self, points):
        self.points = points
    def render(self):
        for index, point in enumerate(self.points):
            print(letter(index) + " - " + str(point.timestamp) + " " + str(point.extra))

def printer(points, xx, yy):
    pointList = PointList(points)
    screen = Screen(xx, yy)
    screen.populate(points = normalize(points))
    screen.render()
    pointList.render()

if __name__ == "__main__":
    """ example of use """
    xx = 10
    yy = 10

    point =   point_generator()
    points = [point_generator() for i in range(0,20)]
    printer(points, xx, yy)
