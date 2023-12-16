"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} {self.next}"

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        head = answer
        current_num = 0

        while current_num or l1 or l2:
            if l1:
                current_num += l1.val
                l1 = l1.next
            if l2:
                current_num += l2.val
                l2 = l2.next

            answer.next = ListNode(current_num % 10)
            answer = answer.next

            # current_num now is a reminder
            if (current_num > 9):
                current_num = 1
            else:
                current_num = 0

        # first Node is not counted
        return head.next

"""
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))
print(Solution().addTwoNumbers(l1, l2))

l1 = ListNode(val=0, next=None)
l2 = ListNode(val=0, next=None)
print(Solution().addTwoNumbers(l1, l2))

