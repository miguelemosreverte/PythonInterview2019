"""
                        #NOTE
                     N-point-operation
                    is a generalization
                            of
                        2-point-op ???

"""

from toolz.itertoolz import sliding_window
from point_ops.great_circle import great_circle

def given_N_points_calculate(function, aggregate_function = sum):
    agg = aggregate_function
    def curry(points):
        return \
        agg(
            function(pointA, pointB)
            for pointA, pointB
            in sliding_window(2, points))
    return curry


from point_ops.great_circle import distance as great_circle_distance
from collections import namedtuple
DistanceTuple = namedtuple("distance", "point, distance")
def compareDistance(pointA, array, aggregate_function = min):
    agg = aggregate_function
    distances = [
                DistanceTuple(
                  point=pointB,
                  distance=great_circle_distance(pointA.coord, pointB.coord)
                )
                for pointB in array]
    return agg(distances, key=lambda p: p.distance)

def closest(pointA, array):
    return compareDistance(pointA, array, aggregate_function = min)

def furthest(pointA, array):
    return compareDistance(pointA, array, aggregate_function = max)




# python -m unittest point_ops.two_point_op
import unittest
from point.utils.generator import point_generator
from point.point import Point
from point.coordinates.coordinates import lat_lng
class Test(unittest.TestCase):
    len = 3
    points = [point_generator(i) for i in range(0,len)]
    def test_closest(self):
        result = closest(Test.points[0], Test.points[1:])
        expected = \
        DistanceTuple(
            point=Point(
                coord=lat_lng(lat=-56, lng=111, r=6371),
                timestamp=1,
                extra={'status': 'HAPPY'}),
            distance=566605.5984774233)
        self.assertEqual(result, expected)

    def test_furthest(self):
        result = furthest(Test.points[0], Test.points[1:])
        expected = \
        DistanceTuple(
            point=Point(
                coord=lat_lng(lat=-76, lng=-134, r=6371),
                timestamp=2,
                extra={'status': 'HAPPY'}),
            distance=711820.7738464935)
        self.assertEqual(result, expected)
