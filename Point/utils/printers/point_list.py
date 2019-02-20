
from point.utils.printers.utils.small import paragraph, letter

class PointList:
    def __init__(self, points):
        self.points = points
    def render(self):
        return paragraph([letter(o)+" - "+str(p.timestamp) + " "+str(p.extra)
         for o, p in enumerate(self.points)])
