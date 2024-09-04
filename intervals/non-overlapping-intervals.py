class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        
        @cache
        def dp(i):
            #compute longest non-overlapping
            curr_start, curr_end = intervals[i]
            #move to other nodes or intervals
            for j in range(i+1, len(intervals)):
                next_start, next_end = intervals[j]
                #non-overlpa
                if curr_end <= next_start:
                    return 1 + dp(j)
                #overlap
                if curr_end > next_end:
                    return dp(j)
            return 1
        #count longest sequence of non-overlapping interval to substract
        #compute min interval to delete
        return len(intervals) - dp(0)