"""
Given head which is a reference node to a singly-linked list.
The value of each node in the linked list is either 0 or 1.
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
"""


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def getDecimalValue(self, head: ListNode) -> int:
        temp = []
        while head is not None:
            temp.append(head.val)
            head = head.next
        res = 0
        count = 0
        for index, i in enumerate(temp):
            res += i * 2 ** count
            count+=1
        return res

    def better(self, head):
        answer = 0
        while head:
            answer = 2*answer+head.val
            head = head.next
        return answer

Solution().getDecimalValue(head = [1,0,1])