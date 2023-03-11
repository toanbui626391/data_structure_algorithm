#problem understanding

#strategy to solve the problem
    #why:
        #finding a_lelft, a_right, b_left and b_right and then logic to find the middle point of a merge sorted array
        #

    #variables:
        #a, b (list): a is shorter list, b is longer list
        #half (int): the first half of total array
        #i, j (int): middle position of a and b
###################################reference solution
from typing import List
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


###############################################reference solution 2
        # a_left, a_right: middle and midle + 1 value of b
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        half = length // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) - 1
        while True:
            i = (l+r)//2
            j = half - i - 2

            nums1_left = nums1[i] if i >= 0 else float("-infinity")
            nums1_right = nums1[i+1] if (i+1) < len(nums1) else float("infinity")
            nums2_left = nums2[j] if j >= 0 else float("-infinity")
            nums2_right = nums2[j+1] if (j+1) < len(nums2) else float("infinity")

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if length % 2:
                    return min(nums1_right, nums2_right)
                return (max(nums1_left, nums2_left)+min(nums1_right, nums2_right))/2

            if nums1_left > nums2_right:
                r = i - 1
            else:
                l = i + 1