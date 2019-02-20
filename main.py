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


from math import cos, sin, pi

from collections import namedtuple
Cartesian = namedtuple("Coord", "x y z") # Scala case-class equivalent
Spherical = namedtuple("Coord", "r θ ψ")
LatLng = namedtuple("Coord", "lat lng r")

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
        return Cartesian(x, y, z)

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
        return LatLng(lat,lng, r)



from math import sqrt, pow, atan2, asin
class CartesianConversions:
    def to_spherical(x, y, z):
        r = sqrt(pow(x,2) + pow(y,2) + pow(z,2))
        θ = atan2(y, x)
        ψ = atan2(sqrt(pow(x,2) + pow(y,2)), z)
        return Spherical(r, θ, ψ)

    def to_lat_lng(x, y, z):
        r = sqrt(pow(x,2) + pow(y,2) + pow(z,2))
        lat = asin(z / r)
        lng = atan2(y, x)
        return LatLng(lat, lng, r)

class LatLngConversions:
    def to_cartesian(lat, lng, r):
        """
        Where R is the approximate radius of earth (e.g. 6371KM).
        Just to make the definition complete, in the Cartesian coordinate system:

        the x-axis goes through long,lat (0,0), so longitude 0 meets the equator;
        the y-axis goes through (0,90);
        and the z-axis goes through the poles.
        """
        x = r * cos(lat) * cos(lng)
        y = r * cos(lat) * sin(lng)
        z = r * sin(lat)
        return Cartesian(x, y, z)

    def to_spherical(lat, lng, r):
        cartesian = LatLngConversions.to_cartesian(lat, lng, r)
        return CartesianConversions.to_spherical(*cartesian)



def test():
    radius = int("10 km".split()[0])
    exampleLatLng = LatLng(
        lat = 0,
        lng = 0,
        r = radius)
    x, y, z = LatLngConversions.to_cartesian(*exampleLatLng)
    r, θ, ψ = LatLngConversions.to_spherical(*exampleLatLng)
    assert x == 10 and y == 0 and  z == 0
    assert r == 10 and θ == 0 and  ψ == 1.5707963267948966
    # check this out!
    # for further reference:
    # https://keisan.casio.com/exec/system/1359533867
