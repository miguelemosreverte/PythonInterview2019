#!/usr/bin/env python
# -*- coding: utf-8 -*-


from point.utils.generator import point_generator

from point.utils.printers.point_list import PointList
from point.utils.printers.screen import Screen
from point.utils.printers.grouped import Grouped

from point.utils.printers.utils.bigger import normalize
from point.utils.printers.utils.small import paragraph, twoline, margin



def printer(points, xx, yy):
    pointList = PointList(points)
    screen = Screen(xx, yy)
    grouped = Grouped(points)
    screen.populate(points = normalize(points))
    return paragraph([
        grouped.render(),
        screen.render(),
        pointList.render()
    ], separator = twoline)



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
