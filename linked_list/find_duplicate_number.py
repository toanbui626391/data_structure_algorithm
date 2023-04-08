"""
strategy to solve the problem
    #why:
        #this is a linked list problem nums[index] equal to node.next
        #using floyd algorithm to find duplicate
            #find first meet node with slow and fast
            #find the second meet. and this is duplicate value

"""
########################reference solution

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        #find the fist mê
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow