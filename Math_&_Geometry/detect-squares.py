"""
Design a system that adds points on a 2D plane
and counts axis-aligned squares that can be
formed with a given query point as one corner.

Example:
  Input:  add([3,10]), add([11,2]), add([3,2]),
          count([11,10])
  Output: 1

Constraints:
  For each diagonal candidate, check both
  remaining corners exist and multiply counts.
"""

import collections
from typing import List


class DetectSquares:

    def __init__(self):
        self.points = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        square_count = 0
        x1, y1 = point

        for (x2, y2), freq in self.points.items():
            x_dist = abs(x1 - x2)
            y_dist = abs(y1 - y2)
            # Diagonal must be equal-length and nonzero.
            if x_dist == y_dist and x_dist > 0:
                corner1 = (x1, y2)
                corner2 = (x2, y1)
                # Both remaining corners must exist.
                if (
                    corner1 in self.points
                    and corner2 in self.points
                ):
                    square_count += (
                        freq
                        * self.points[corner1]
                        * self.points[corner2]
                    )

        return square_count
