"""
Problem:
Permutations - Given an array of distinct integers,
return all possible permutations.

Examples:
Input:
nums = [1, 2, 3]

Output:
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1],
 [3, 1, 2], [3, 2, 1]]

Constraints:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All integers in nums are unique.
"""

from typing import List


class Solution:
    """
    Standard backtracking solution using a 'used' array
    to keep track of elements already in the current path.
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all permutations of the input list.
        """
        results = []
        path = []
        # 'used' flags to avoid picking the same element twice.
        used = [False] * len(nums)

        def backtrack():
            # Base case: path length matches input length.
            if len(path) == len(nums):
                # Append a copy of the current path.
                results.append(path[:])
                return

            for i in range(len(nums)):
                # Skip if the element is already used.
                if used[i]:
                    continue

                # 1. Choose: Mark as used and add to path.
                used[i] = True
                path.append(nums[i])

                # 2. Explore: Recurse to find the next element.
                backtrack()

                # 3. Un-choose: Undo choice for next iteration.
                path.pop()
                used[i] = False

        backtrack()
        return results


if __name__ == "__main__":
    # Test cases optimized for 60-char wide screens.
    sol = Solution()
    test_nums = [1, 2, 3]
    output = sol.permute(test_nums)
    print(f"Input: {test_nums}")
    print(f"Output: {output}")
