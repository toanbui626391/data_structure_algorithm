class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if not intervals: return []
        intervals.sort()

        unique = []
        last = intervals[0]
        for cur in intervals:
            #find overlap and merge
            if cur[0] <= last[1]:
                last[1] = max(last[1], cur[1])
            else: #no overlapp
                #append last and update last to curr
                unique.append(last)
                last = cur
        #append final last
        unique.append(last)
        return unique
                    