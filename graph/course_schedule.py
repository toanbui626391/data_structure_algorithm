"""
strategy to solve the problem
    problem:
        given number of course (int) ad a list of list present prerequisites. Check that can we complete all course. Or we do not have circle graph
    why:
        using dfs
            build preMap {course: [courses_to_completed]}
            check have circle from course or not
            #after check we have to remove course from visited and node is not circle

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
            #remove course from visited for next course check and mark course can be completed 
            visiting.remove(crs)
            preMap[crs] = [] #update empty list for node which it not cycle so that we will not process that node again
            return True
        #if one of the course can not complete return False, all course complete return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
