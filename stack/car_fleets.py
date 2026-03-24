"""
Problem: Car Fleet

There are n cars going to a target. Each car has
a position and speed. A car fleet is one or more
cars driving together at the same speed. Return
the number of car fleets that will arrive.

Example:
  Input:  target=12, position=[10,8,0,5,3], 
          speed=[2,4,1,1,3]
  Output: 3

Approach: Monotonic Stack
  - Sort cars by position descending (closest to
    target first).
  - Calculate arrival time: (target - pos) / speed
  - If a car arrives in less or equal time than
    the car ahead of it (stack top), it catches up
    and forms a fleet. Otherwise, it forms a new
    fleet (push to stack).
"""

from typing import List


class Solution:
    def carFleet(
        self,
        target: int,
        position: List[int],
        speed: List[int],
    ) -> int:
        
        # Combine and sort by position, closest first
        cars = sorted(zip(position, speed), reverse=True)
        
        # Stack will store the arrival times of fleets
        stack = []

        for pos, spd in cars:
            arrival_time = (target - pos) / spd
            
            # Push arrival time
            stack.append(arrival_time)
            
            # If our current car arrives faster or at
            # the same time as the fleet ahead of it,
            # they merge. The slower fleet dictates
            # the arrival time, so we pop the faster
            # one we just added.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        # The number of unique arrival times left in
        # the stack is the number of fleets.
        return len(stack)
