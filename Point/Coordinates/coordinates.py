#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import cos, sin, pi

from collections import namedtuple
cartesian = namedtuple("Cartesian", "x y z") # Scala case-class equivalent
spherical = namedtuple("Spherical", "r θ ψ")
lat_lng = namedtuple("LatLng", "lat lng r")

"""
To be noted:  "Lat/Lon/Alt" is just another name for spherical coordinates,
and phi/theta/rho are just another name for latitude, longitude, and altitude. :)
(A minor difference: altitude is usually measured from the surface of the sphere;
rho is measured from the center -- to convert, just add/subtract the radius of the sphere.)
"""


class SphericalConversions: # Scala companion-object equivalent: It's a JS module
    def to_cartesian(r, θ, ψ):
        x = r * cos(θ) * sin(ψ)
        y = r * sin(θ) * sin(ψ)
        z = r * cos(ψ)
        return cartesian(x, y, z)

    def to_lat_lng(r, θ, ψ):
        π = pi
        def latitude():
            if 0 <=  ψ  < π/2:  return 90 - (180 * ψ)/π
            if  ψ  ==  π/2:     return 0
            if π/2 <  ψ  <= π:  return ((180 * ψ)/π - 90)
        def longitude():
            if θ  ==  0:        return 0
            if 0 <  θ  < π:     return ((180 * θ)/π)
            if θ  ==  π:        return 180
            if π <  θ  < 2*π:   return (360 - (180 * θ)/π)

        lat, lng = (latitude(), longitude())
        return lat_lng(lat,lng, r)



from math import sqrt, pow, atan2, asin
class CartesianConversions:
    def to_spherical(x, y, z):
        r = sqrt(pow(x,2) + pow(y,2) + pow(z,2))
        θ = atan2(y, x)
        ψ = atan2(sqrt(pow(x,2) + pow(y,2)), z)
        return spherical(r, θ, ψ)

    def to_lat_lng(x, y, z):
        r = sqrt(pow(x,2) + pow(y,2) + pow(z,2))
        lat = asin(z / r)
        lng = atan2(y, x)
        return lat_lng(lat, lng, r)

class LatLngConversions:
    def to_cartesian(lat, lng, r):
        """
        Where R is the approximate radius of earth (e.g. 6371KM).
        Just to make the definition complete, in the cartesian coordinate system:

        the x-axis goes through long,lat (0,0), so longitude 0 meets the equator;
        the y-axis goes through (0,90);
        and the z-axis goes through the poles.
        """
        x = r * cos(lat) * cos(lng)
        y = r * cos(lat) * sin(lng)
        z = r * sin(lat)
        return cartesian(x, y, z)

    def to_spherical(lat, lng, r):
        cartesian = LatLngConversions.to_cartesian(lat, lng, r)
        return CartesianConversions.to_spherical(*cartesian)


"""a more OOP approach with
_from_ methods
instead of
_to_ methods
"""


class Cartesian:
    """       cartesian
              /     \
             /       \
            /       to_cartesian
           /           \
        to_cartesian    \
        /                \
    lat_lng              spherical

    """
    def from_spherical(spherical):
        return SphericalConversions.to_cartesian(*spherical)
    def from_lat_lng(lat_lng):
        return LatLngConversions.to_cartesian(*lat_lng)

class Spherical:
    """        spherical
              /     \
             /       \
            /       to_spherical
           /           \
        to_spherical    \
        /                \
    cartesian           lat_lng

    """
    def from_cartesian(cartesian):
        return CartesianConversions.to_spherical(*cartesian)
    def from_lat_lng(lat_lng):
        return LatLngConversions.to_spherical(*lat_lng)

class LatLng:
    """        lat_lng
              /     \
             /       \
            /       to_lat_lng
           /           \
        to_lat_lng      \
        /                \
    cartesian           spherical

    """
    def from_spherical(spherical):
        return SphericalConversions.to_lat_lng(*spherical)
    def from_cartesian(cartesian):
        return CartesianConversions.to_lat_lng(*cartesian)

# python -m unittest point.coordinates.coordinates
import unittest
class Test(unittest.TestCase):
    def test(self):
        radius = int("10 km".split()[0])
        exampleLatLng = lat_lng(
            lat = 0,
            lng = 0,
            r = radius)
        x, y, z = Cartesian.from_lat_lng(exampleLatLng)
        r, θ, ψ = Spherical.from_lat_lng(exampleLatLng)
        assert x == 10 and y == 0 and  z == 0
        assert r == 10 and θ == 0 and  ψ == 1.5707963267948966
        # check this out!
        # for further reference:
        # https://keisan.casio.com/exec/system/1359533867
