# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # use slow and fast pointers to find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # from the slow (middle) point to the fast (end) point, we must reverse the linked list
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # then, we can have one pointer at the head, one pointer at the start of our new reversed linked list, and just add the two numbers and traverse forward, keeping track of the maximum 
        maxSum = -1
        first, second = head, prev
        while second:
            currSum = first.val + second.val
            maxSum = max(maxSum, currSum)
            first, second = first.next, second.next

        return maxSum