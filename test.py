
import os
test_list =[
  "point.coordinates.coordinates"
, "point.utils.generator"
, "point.utils.printer"
, "point_ops.great_circle"
, "point_ops.two_point_op"
]

for test in test_list:
    os.system(f"python -m unittest -v {test}")
