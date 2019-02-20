
from itertools import groupby
from point.utils.printers.utils.small import paragraph, small_margin, margin, twoline

# NOTE it's again like Scala Companion Object:
# A JS module full of pure functions
# What this semantics do is achieve guarantees during read
# so that the developers _knows_ this functions are pure
class Helper:
    th = f"""
{margin}status |       point    |       time
{margin}------------------------------------------
{margin}       | lat      lng   |
    """


    td = lambda status, lat, lng, timestamp:\
        f"\t\t{status}  | {lat}\t{lng}\t|\t {timestamp}"


    renderGroup = lambda status, rest:\
            paragraph([Helper.td(status, lat, lng, timestamp)
                for ((lat, lng, r), timestamp, extra) in rest]
                + [f"{margin}------------------------------------------"]
                , separator = small_margin)

    group_points = lambda points, predicate = lambda x: x.extra["status"]:\
        [
        (k,rest) for k,rest in
        [(k,list(rest)) for (k,rest) in groupby(sorted(points, key = predicate), predicate)]]

class Grouped:
    def __init__(self, points):
        self.points = points


    def render(self):

        by_status = Helper.group_points(self.points, predicate = lambda x: x.extra["status"])

        table = (
            margin + Helper.th
            + paragraph(
            [Helper.renderGroup(status, rest)
            for status, rest in by_status])
            + twoline)
        return table
