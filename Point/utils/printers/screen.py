
from point.utils.printers.utils.small import paragraph, letter
from point.utils.printers.utils.bigger import ascii_art

class Screen:

    def __init__(self, xx, yy):
        self.xx = xx
        self.yy = yy
        self.screen = [[ascii_art(x,y, xx, yy) for x in range(0,xx+1)]
        for y in range(yy, 0-1, -1)]

    def populate(self, points):
        xx = self.xx
        yy = self.yy
        for index, ((lat, lng, r), timestamp, extra) in enumerate(points):
            x = int(lat * xx)
            y = int(lng * yy)
            self.screen[y][x] = ascii_art(x, yy-y, xx, yy, letter(index))

    def render(self):
        return paragraph([" ".join(t) for t in self.screen])
