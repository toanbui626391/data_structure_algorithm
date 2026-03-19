"""
There are n cars going to a target. Each car has
a position and speed. A car fleet is one or more
cars driving together at the same speed. Return
the number of car fleets that will arrive.

Example:
  Input:  target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3]
  Output: 3

Constraints:
  Sort by descending position; a slower leading car captures
  faster trailing cars into the same fleet.
"""

from typing import List


class Solution:
    def carFleet(
        self,
        target: int,
        position: List[int],
        speed: List[int],
    ) -> int:
        # Sort descending so we process from front to back.
        pair = sorted(
            [(pos, spd) for pos, spd in zip(position, speed)],
            reverse=True,
        )
        stack = []
        for pos, spd in pair:
            time = (target - pos) / spd
            # A faster car joins the leader's fleet if it arrives
            # no later than the car already at stack top.
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)
