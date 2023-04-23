#problem undertanding

#strategy to solve the problem
    #why:
        #because of set method policy we always have TimeMap[key] is sorted
        #get(key, time): return value which associate with the key and largest time_prev given time.
            #using custom binary search in this case

        #collector which each key have values is list. Therefore use defaultdict(list)
    #variables:
        #keeper = defaultdict(list)

###################################################reference solution
from collections import defaultdict
class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keeper = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keeper[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keeper[key]

        l, r = 0, len(values) - 1
       
        while l <= r:
            mid = (l+r)//2
            if timestamp >= values[mid][1]:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res 