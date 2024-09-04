class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        #non-overlap sorted interval
        for interval in intervals:
            #no overlap, newInterval on the right -> append interval
            if interval[1] < newInterval[0]:
                result.append(interval)
            #no overlap newInverval on the left
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            #overlap then merge
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        
        result.append(newInterval); 
        return result