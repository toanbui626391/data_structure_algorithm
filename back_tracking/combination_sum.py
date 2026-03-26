"""
Problem:
Combination Sum - Given an array of distinct integers
candidates and a target, return all unique combinations
where the chosen numbers sum to target. Numbers may be
chosen unlimited times.

Examples:
Input:
candidates = [2, 3, 6, 7], target = 7

Output:
[[2, 2, 3], [7]]

Constraints:
- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All candidates are unique.
- 1 <= target <= 40
"""

from typing import List


class Solution:
    """
    Standard backtracking solution using a 'for' loop
    to explore choices starting from the current index.
    """

    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        """
        Generates all unique combinations that sum to target.
        """
        results = []
        path = []

        def backtrack(remainder: int, start_index: int):
            # Base case: valid combination found.
            if remainder == 0:
                results.append(path[:])
                return

            # Base case: target exceeded.
            if remainder < 0:
                return

            for i in range(start_index, len(candidates)):
                # 1. Choose: Add candidate to path.
                path.append(candidates[i])

                # 2. Explore: Recurse with same index (allows reuse).
                backtrack(remainder - candidates[i], i)

                # 3. Un-choose: Undo choice for next sibling.
                path.pop()

        backtrack(target, 0)
        return results


if __name__ == "__main__":
    # Test cases optimized for 60-char wide screens.
    sol = Solution()
    test_candidates = [2, 3, 6, 7]
    test_target = 7
    output = sol.combinationSum(test_candidates, test_target)
    print(f"Candidates: {test_candidates}")
    print(f"Target: {test_target}")
    print(f"Output: {output}")
