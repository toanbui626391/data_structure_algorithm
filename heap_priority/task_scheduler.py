
import heapq
from collections import deque, Counter
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        #using max heap because we want to process task with which have most frequent
        maxHeap = [-cnt for cnt in count.values()] #number of task for each type of task
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]. cnt: - (number of task of this type left), when we can process it
        while maxHeap or q: #we need task to schedule
            time += 1

            if not maxHeap: #to task to process
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap) #process job
                if cnt: #stil have job appen number of job left and the time to process it next time
                    q.append([cnt, time + n])
            if q and q[0][1] == time: #push the job which can be process to the heap again
                heapq.heappush(maxHeap, q.popleft()[0])
        return time