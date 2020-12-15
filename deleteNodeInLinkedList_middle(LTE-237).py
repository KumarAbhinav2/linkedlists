"""
Write a function to delete a node in a singly-linked list.
You will not be given access to the head of the list,
instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.


Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9
after calling your function.

Input: head = [1,2,3,4], node = 3
Output: [1,2,4]
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        while node.next:
            node.val = node.next.val
            if node.next.next:
                node = node.next
            else:
                node.next = None