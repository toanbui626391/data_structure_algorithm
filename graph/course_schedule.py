"""
strategy to solve the problem
    problem: given number of course (int) ad a list of list present prerequisites. Check that can we complete all course. Or we do not have circle graph
"""
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # init preMap
        preMap = {i: [] for i in range(numCourses)}

        #build premap
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            #if visited node more than once return False
            if crs in visiting:
                return False
            #a course is no prerequisite can complete
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            #if one of the child node can not be complete than the parent node also can not be completet
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            #clean the current node to prepare to process the parent node and return True    
            visiting.remove(crs)
            preMap[crs] = []
            return True
        #if one of the course can not complete return False, all course complete return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
