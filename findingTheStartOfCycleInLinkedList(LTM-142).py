"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer. Internally, pos is used to denote the index of the
node that tail's next pointer
is connected to. Note that pos is not passed as a parameter.
Notice that you should not modify the linked list.


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycleStart(self, head):
        # take two pointer both starting from head
        slow = fast = head
        # loop till cycle is not even there
        while fast and fast.next:
            # increment slow one step
            slow = slow.next
            # increment fast two steps
            fast = fast.next.next
            # that means cycle is there
            if slow == fast:
                break
        # reassign slow to head
        slow = head
        # loop till both slow and fast meet
        while slow != fast:
            # increment both 1 step
            slow = slow.next
            fast = fast.next
        # the place where they meet is the start of the loop
        return slow

