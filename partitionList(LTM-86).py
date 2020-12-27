"""
Given a linked list and a value x, partition it such that all nodes less than x come before
nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x):
        # Initialising two pointers
        right = right_head = ListNode()
        left = left_head = ListNode()
        while head:
            if head.val < x:
                # updating left pointer
                left.next = ListNode(head.val)
                left = left.next
            else:
                # updating right pointer
                right.next = ListNode(head.val)
                right = right.next
            head = head.next
        # merging the lists
        left.next = right_head.next
        return left_head.next

    # Time Complexity: O(n)
    # Space Complexity: O(1)

