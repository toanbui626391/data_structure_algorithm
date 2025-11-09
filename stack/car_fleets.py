#problem understanding

#strategy to solve the problem
    #variable
        #pair (position, speed) (list) decrease or reverse: 
            #to keep track of start position and speed of cars
            #because their is only one laind
        #stack (time to complete remaining range): 
            #number of remain element is the number of carfleet form
        #why using if in this case:
            # because we only watn to pop car which is forming carfleet after
            # the first car in the carfleet
##########################################reference solution
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    
#######################################reference solution v2
# use stack to keep time the last one is the last car fleet time.
# therefore len(stack) is number of carfleet form
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)
        stack = []
        for p, s in pair:
            time = (target-p)/s
            # stack.append((target-p)/s)
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)