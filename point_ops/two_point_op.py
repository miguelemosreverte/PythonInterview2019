from toolz.itertoolz import sliding_window
from point.utils.generator import point_generator

def given_two_points_calculate(function, aggregate_function = sum):
    agg = aggregate_function
    def curry(points):
        return \
        agg(
            function(pointA, pointB)
            for pointA, pointB
            in sliding_window(2, points))
    return curry


from point_ops.great_circle import great_circle
def distance(pointA, pointB):
    a = (pointA.coord.lat, pointA.coord.lng)
    b = (pointB.coord.lat, pointB.coord.lng)
    return great_circle(*a, *b, radius=60.0)


def time_delta(pointA, pointB):
    a = pointA.timestamp
    b = pointB.timestamp
    return b - a


def velocity(pointA, pointB):
    nautic_miles = distance(pointA, pointB)
    hours = time_delta(pointA, pointB)
    return nautic_miles / hours

trayectory_distance = given_two_points_calculate(distance)
trayectory_time =     given_two_points_calculate(time_delta)
from statistics import mean
trayectory_velocity = given_two_points_calculate(velocity, mean)

# python -m unittest point_ops.two_point_op
import unittest
class Test(unittest.TestCase):
    len = 3
    points = [point_generator(i) for i in range(0,len)]
    def test_trayectory_time(self):
        self.assertEqual(
            trayectory_time(Test.points), Test.len-1)

    def test_trayectory_distance(self):
        self.assertEqual(
            trayectory_distance(Test.points), 7834.998250810107)

    def test_trayectory_velocity(self):
        r = trayectory_velocity(Test.points)
        for point in Test.points:
            print(point.coord)
        self.assertEqual(
            trayectory_velocity(Test.points), 3917.4991254050533)
