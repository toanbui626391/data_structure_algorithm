"""
Given numCourses and a list of prerequisite pairs,
determine if you can finish all courses (i.e., the
dependency graph is acyclic).

Example:
  Input:  numCourses=2, prerequisites=[[1,0]]
  Output: True

Constraints:
  DFS with a visiting set detects cycles in the prereq graph.
"""

from typing import List


class Solution:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
    ) -> bool:
        # Map each course to its list of prerequisites.
        pre_map = {idx: [] for idx in range(numCourses)}

        for course, prereq in prerequisites:
            pre_map[course].append(prereq)

        # Tracks courses currently on the DFS path (cycle check).
        visiting = set()

        def dfs(course):
            # Seeing the same node twice means a cycle exists.
            if course in visiting:
                return False
            # No prerequisites; this course can be completed.
            if pre_map[course] == []:
                return True

            visiting.add(course)
            for prereq in pre_map[course]:
                if not dfs(prereq):
                    return False
            # Remove from path; mark prerequisites as cleared.
            visiting.remove(course)
            pre_map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
