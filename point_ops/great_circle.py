#-----------------------------------------------------------------------
# https://introcs.cs.princeton.edu/python/12types/greatcircle.py
#-----------------------------------------------------------------------

import sys
import math

from point.coordinates.coordinates import lat_lng

def great_circle(x1, y1, x2, y2, radius):

    # The following formulas assume that angles are expressed in radians.
    # So convert to radians.
    x1 = math.radians(x1)
    y1 = math.radians(y1)
    x2 = math.radians(x2)
    y2 = math.radians(y2)

    # Compute using the law of cosines.

    # Great circle distance in radians
    angle = math.acos(math.sin(x1) * math.sin(x2) \
             + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

    # Convert back to degrees.
    angle = math.degrees(angle)

    arc_length = radius * angle
    # check this out!
    # for further reference:
    # https://www2.clarku.edu/faculty/djoyce/trig/angle.html
    return arc_length



def distance(pointA, pointB):
    (lat1, lng1, r1) = pointA
    (lat2, lng2, r2) = pointB
    if r1 == r2:
        return great_circle(lat1, lng1, lat2, lng2, radius=r1)
    else: raise Exception('Points should share their radius!')

# python -m unittest point_ops.great_circle
import unittest
class Test(unittest.TestCase):
    def test(self):
        def great_circle_earth_nautic_miles(a, b):
            # Each degree on a great circle of Earth is 60 nautical miles.
            return great_circle(*a, *b, radius=60.0)
        result = great_circle_earth_nautic_miles((0, 0), (45, 90))
        assert result == 5400
        # check this out!
        # for further reference:
        # http://edwilliams.org/gccalc.htm
