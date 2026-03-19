"""
Given a list of airline tickets as [from, to] pairs,
reconstruct the itinerary starting from "JFK" using
all tickets exactly once. Return the lexicographically
smallest itinerary if multiple exist.

Example:
  Input:  tickets=[["MUC","LHR"],["JFK","MUC"],
          ["SFO","SJC"],["LHR","SFO"]]
  Output: ["JFK","MUC","LHR","SFO","SJC"]

Constraints:
  Sort destinations in reverse so .pop() gives lexicographic order.
"""

from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def findItinerary(
        self, tickets: List[List[str]]
    ) -> List[str]:
        # Build adjacency list sorted in reverse for pop() order.
        graph = defaultdict(list)
        for src, dest in sorted(tickets, reverse=True):
            graph[src].append(dest)

        itinerary = []

        @cache
        def dfs(src):
            # Exhaust all destinations from this source first.
            while graph[src]:
                dfs(graph[src].pop())
            # Append after all children are processed (post-order).
            itinerary.append(src)

        dfs("JFK")
        # Post-order DFS builds the list in reverse.
        return itinerary[::-1]
