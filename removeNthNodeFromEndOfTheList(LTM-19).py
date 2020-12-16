"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthNode(self, head, n):
        # Taking a dummy node to point to head
        dummy = ListNode()
        # Both slow and fast pointers will start from dummy pointer
        slow = fast = dummy
        dummy.next = head
        # move fast to n steps ahead
        for _ in range(n):
            fast = fast.next
        # while fast reaches end, slow will be 1 node behind the nth node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        # return before head
        return dummy.next
