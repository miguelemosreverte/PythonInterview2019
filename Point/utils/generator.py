#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
from collections import namedtuple
from Point.Coordinates.coordinates import lat_lng

Point = namedtuple("Point", "coord timestamp extra")



def point_generator():
    gen = lambda min,max: random.randint(min, max)
    lat = gen(-90, 90)
    lng = gen(-180, 180)
    r = 20
    timestamp = gen(0, 2359) #HHMM
    statuses = [
        "HAPPY",
        "TIRED"
    ]
    status = statuses[gen(0,1)]
    extra = {'status': status}

    example_point = Point(lat_lng(lat, lng, r), timestamp, extra)
    return example_point

# point = point_generator()
# array = [point_generator() for i in range(0,20)]
