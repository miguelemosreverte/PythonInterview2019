

"""

bigger utils

"""

def normalize(points):
    from point.point import Point
    from point.coordinates.coordinates import lat_lng
    return  [
    Point(
      lat_lng(
        lat = (point.coord.lat/(90*2))+0.5,
        lng = (point.coord.lng/(180*2))+0.5,
        r=2
      ),
      point.timestamp,
      point.extra
    ) for point in points]


def ascii_art(x,y, xx, yy, value = " "):
    # "edge" cases, quite literally!
    left_top = lambda x,y: x == 0 and y == yy
    right_bottom = lambda x,y: x == xx and y == 0
    if left_top(x,y): return " Y ^ "
    if right_bottom(x,y): return " >"
    if y == 0 and x == 0: return " X - "
    if y == 0: return "- "
    if x == 0: return "   |"+ value
    return value
