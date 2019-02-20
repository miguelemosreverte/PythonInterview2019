#-----------------------------------------------------------------------
# https://introcs.cs.princeton.edu/python/12types/greatcircle.py
#-----------------------------------------------------------------------

import sys
import math

from coordinates import lat_lng

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

def great_circle_earth_nautic_miles(lat, lng):
    # Each degree on a great circle of Earth is 60 nautical miles.
    return great_circle(*lat, *lng, radius=60.0)

def test():
    a = lat_lng(0, 0, None)
    b = lat_lng(45, 90, None)
    result = great_circle_earth_nautic_miles(
        (a.lat, a.lng), (b.lat, b.lng)
    )
    assert result == 5400
    # check this out!
    # for further reference:
    # http://edwilliams.org/gccalc.htm
