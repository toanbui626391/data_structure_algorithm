"""
Given intervals and queries, for each query find
the size of the smallest interval that contains
it. Return -1 if no such interval exists.

Example:
  Input:  intervals=[[1,4],[2,4],[3,6],[4,4]],
          queries=[2,3,4,5]
  Output: [3,3,1,4]

Constraints:
  Sort both; use a min-heap keyed by interval
  size, pushing intervals that cover the query
  and popping those that no longer do.
"""
