"""
Given numCourses and a list of prerequisite pairs,
determine if you can finish all courses (i.e., the
dependency graph is acyclic).

Example:
  Input:  numCourses=2, prerequisites=[[1,0]]
  Output: True

Constraints:
  DFS with a visiting set detects cycles in the graph.
  BFS using Kahn's algorithm (topological sort)
  can also be used.
"""

from collections import deque
from typing import List


class SolutionDFS:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
    ) -> bool:
        # Map each course to its list of prerequisites.
        pre_map = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            pre_map[course].append(prereq)

        # Track state: 0=Unvisited, 1=Visiting, 2=Visited
        states = [0] * numCourses

        def dfs(course):
            # Seeing a visiting node means a cycle.
            if states[course] == 1:
                return False
            # Fully visited node is already safe.
            if states[course] == 2:
                return True

            # Mark as visiting.
            states[course] = 1

            for prereq in pre_map[course]:
                if not dfs(prereq):
                    return False

            # Mark as visited.
            states[course] = 2
            return True

        for course in range(numCourses):
            if states[course] == 0:
                if not dfs(course):
                    return False

        return True


class SolutionBFS:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
    ) -> bool:
        # Build adjacency list & in-degree counts.
        adj_list = {i: [] for i in range(numCourses)}
        in_degrees = {i: 0 for i in range(numCourses)}

        for course, pre in prerequisites:
            adj_list[pre].append(course)
            in_degrees[course] += 1

        # Queue courses with no prerequisites.
        queue = deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        completed = 0

        # Process courses via BFS.
        while queue:
            curr = queue.popleft()
            completed += 1

            for neighbor in adj_list[curr]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        # True if we were able to take all courses.
        return completed == numCourses
