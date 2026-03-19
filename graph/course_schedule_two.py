"""
Given numCourses and prerequisites, return a valid
ordering of courses to finish all of them, or an
empty array if it is impossible.

Example:
  Input:  numCourses=4,
          prerequisites=[[1,0],[2,0],[3,1],[3,2]]
  Output: [0,2,1,3] or another valid order

Constraints:
  Topological sort via DFS; a cycle makes it impossible.
"""
