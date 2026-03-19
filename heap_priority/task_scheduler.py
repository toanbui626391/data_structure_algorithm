"""
Given tasks and a cooldown n, return the minimum
number of intervals needed to finish all tasks.
Between two same-type tasks, at least n intervals
must pass.

Example:
  Input:  tasks=["A","A","A","B","B","B"], n=2
  Output: 8

Constraints:
  Process the most frequent task first to minimize idle time.
"""

import heapq
from collections import deque, Counter
from typing import List


class Solution:
    def leastInterval(
        self, tasks: List[str], n: int
    ) -> int:
        count = Counter(tasks)
        # Negate counts to use Python's min-heap as max-heap.
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        # Queue holds (remaining_count, earliest_process_time).
        cooldown_queue = deque()
        while max_heap or cooldown_queue:
            time += 1

            if not max_heap:
                # Jump time forward when no task is ready.
                time = cooldown_queue[0][1]
            else:
                cnt = 1 + heapq.heappop(max_heap)
                # Reschedule if more of this task type remain.
                if cnt:
                    cooldown_queue.append([cnt, time + n])

            # Re-add tasks whose cooldown has expired.
            if cooldown_queue and cooldown_queue[0][1] == time:
                heapq.heappush(
                    max_heap, cooldown_queue.popleft()[0]
                )
        return time
