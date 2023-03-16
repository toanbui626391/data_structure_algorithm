#strategy to solve the problem:
    #why:
        #using slow and fast strategy to find middle. slow.next will be head of the second half
            #slow behind and move one while fast is first and move twice
        #reverse the second half. remember to change from slow.next = None
        #we do need temp1, temp2 for merge two linked list together. because we we need to update first and second for next iteration

    #variables:
        #slow and fast (ListNode): to find middle node

    #error note:
        #condition to stop slow, fast strategy
            #while fast and fast.next
        #condition for merge. because with slow and fast pointer second half is always smaller than first half
            #while second:
        #rember to complete the first half after find middle
            #slow.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2