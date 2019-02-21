#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from collections import namedtuple
from point.coordinates.coordinates import lat_lng

Point = namedtuple("Point", "coord timestamp extra")


def point_generator(seed):
    random.seed(seed) # NOTE determinism allows validation
    global counter # NOTE dangerous but valid due to context simplicity
    gen = lambda min,max: random.randint(min, max)
    lat = gen(-90, 90)
    lng = gen(-180, 180)
    r = int("6371 km is the Earth radius.".split()[0])
    timestamp = seed
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


# python -m unittest point.utils.generator
import unittest
class Test(unittest.TestCase):
    def test(self):
        point = point_generator(1)
        assert point == Point(  coord=lat_lng(lat=-56, lng=111, r=6371),
                                timestamp=1,
                                extra={'status': 'HAPPY'})
