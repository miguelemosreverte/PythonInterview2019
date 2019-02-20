#!/usr/bin/env python
# -*- coding: utf-8 -*-


import string
from collections import namedtuple
from point.coordinates.coordinates import lat_lng
from point.utils.generator import point_generator
from point.point import Point




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
        return "\n".join([" ".join(t) for t in self.screen])

class PointList:
    def __init__(self, points):
        self.points = points
    def render(self):
        return "\n".join([letter(o)+" - "+str(p.timestamp) + " "+str(p.extra)
         for o, p in enumerate(self.points)])

def printer(points, xx, yy):
    pointList = PointList(points)
    screen = Screen(xx, yy)
    screen.populate(points = normalize(points))
    return "\n".join([
        screen.render(),
        pointList.render()
    ])


to_singleline = \
    lambda m: " ".join(m.replace('\n', ' ').split()).strip()

# python -m unittest point.utils.printer
import unittest
class Test(unittest.TestCase):
    def test(self):
        """ example of use """
        xx = 10
        yy = 10

        point =   point_generator(1)
        points = [point_generator(i) for i in range(0,2)]
        result = printer(points, xx, yy)
        expected = """
             Y ^
               |
               |
               |
               |
               |          A
               |
               |
               |  B
               |
             X -  -  -  -  -  -  -  -  -  -   >
            A - 0 {'status': 'HAPPY'}
            B - 1 {'status': 'HAPPY'}
        """
        a = to_singleline(result)
        b = to_singleline(expected)
        assert a == b
if __name__ == "__main__":
    """ example of use """
    xx = 10
    yy = 10

    point =   point_generator()
    points = [point_generator(i) for i in range(0,20)]
    print(printer(points, xx, yy))
    # NOTE side-effects should be as close to main as possible
