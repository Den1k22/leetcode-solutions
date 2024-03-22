"""
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.
 
 Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 
Follow up: Could you do it in O(n) time and O(1) space?
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        slow_arr = []

        while fast != None and fast.next != None:
            slow_arr.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast != None:
            slow = slow.next

        slow_arr = slow_arr[::-1]

        for i in range(len(slow_arr)):
            if slow_arr[i] != slow.val:
                return False

            slow = slow.next

        return True

"""
Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""
