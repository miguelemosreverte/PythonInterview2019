
import os
test_list =[
  "point.coordinates.coordinates"
, "point.utils.generator"
, "main"
, "point_ops.great_circle"
, "point_ops.two_point_op"
, "point_ops.N_points_op"
]

for test in test_list:
    os.system(f"python -m unittest -v {test}")
