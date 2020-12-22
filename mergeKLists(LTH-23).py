"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
"""
from queue import PriorityQueue

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        out = head = ListNode()
        # Idea is to put min of heads from all 3 lists into PriorityQueue first
        # and then keep on updating the heads (min value heads)
        q = PriorityQueue()
        for i, l in enumerate(lists):
            # If head is not None
            if l:
                # fetch min val node first, setting the priority
                # Putting this i incase we get same value nodes then based on index get the value
                # Other u will face error in python3
                q.put((l.val, i, l))
        # Iterate till out queue is empty
        while not q.empty():
            val, i, node = q.get()
            # create a new node with val and make 'out' points to it
            out.next = ListNode(val)
            out = out.next
            node = node.next
            # check if we have valid next node
            if node:
                # put again in queue
                q.put((node.val, i, node))
        # Since head is pointing to out with initial val 0
        return head.next

    # Time Complexity: O(Nlogk), k is the number of linked lists, O(logk) for each pop and insertion to PriorityQueue
        # There are N such nodes in lists so O(Nlogk)
    # Space Complexity: O(N), for creating new out list