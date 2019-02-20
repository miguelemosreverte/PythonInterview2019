#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
1) Define "great circle" distance
2) Having a point (2D as in lat,lng) series, a timestamp, and extra data
    .
    .    (1,2 at 2pm)-----(2,2 at 3pm)-----(3,2 at 4pm )
    .   {status:HAPPY}   {status:TIRED}   {status:TIRED}
    .
 Y  .
    .  .  .  .  .  .  .  .  .  .  .  .  .  .
       X

      - Calculate the final distance in meters of the total trayectory
      - Calculate the total trayectory time
      - Calculate the velocity between points
      - Calculate average velocity
      - Group common data

      status |    point     |  time
      -----------------------------
       HAPPY | [(1,2)]      | [(2pm, 3pm)]
       TIRED | [(2,2, 3,2)] | [(3pm, 4pm)]

3) Having a point, and an array of points:
    define closest, furthest,
    radious of circle that starts at central point and ends at furthest point
"""


#!/usr/bin/env python
# -*- coding: utf-8 -*-


from point.utils.generator import point_generator

from point.utils.printers.point_list import PointList
from point.utils.printers.plot import Plot
from point.utils.printers.grouped import Grouped

from point.utils.printers.utils.bigger import normalize
from point.utils.printers.utils.small import *

from point_ops.two_point_op import \
trayectory_distance,\
trayectory_time,\
trayectory_velocity



def procedural_documentation(points, xx, yy):
    pointList = PointList(points)
    plot = Plot(xx, yy)
    grouped = Grouped(points)
    plot.populate(points = normalize(points))
    return paragraph([
        f"""
        {margin}Here is a proof of grouping by data.
        """,
        grouped.render(),
        f"""
        {margin}Here we can preview a normalized view
        {margin}of the lat/lng coordinates.
        """,
        plot.render(),
        f"""
        {margin}Finally we have the data for each coordinate.
        """,
        pointList.render(),
        f"{margin}So, story made, short, we have that a trayectory that took",
        f"{margin}      {str(trayectory_distance(points))} nautic miles",
        f"{margin}      {str(trayectory_time(points))} hours",
        f"{margin}at {str(trayectory_velocity(points))} at nautic miles per hour",
        ""

    ], separator = twoline)



# python -m unittest point.utils.procedural_documentation
import unittest
class Test(unittest.TestCase):
    def test(self):
        """ example of use """
        xx = 10
        yy = 10

        point =   point_generator(1)
        points = [point_generator(i) for i in range(0,2)]
        result = procedural_documentation(points, xx, yy)
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

    point =   point_generator(1)
    points = [point_generator(i) for i in range(0,6)]
    print(procedural_documentation(points, xx, yy))
    # NOTE side-effects should be as close to main as possible
