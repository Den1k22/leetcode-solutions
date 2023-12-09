"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in a strictly increasing order.
"""

from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        nums_length = len(nums)
        if nums_length == 0:
            return None
        
        mid_point = nums_length // 2
        return TreeNode(
            nums[mid_point], 
            self.sortedArrayToBST(nums[:mid_point]), self.sortedArrayToBST(nums[mid_point + 1 :])
        )
        
    
"""
Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""

nums = [-10,-3,0,5,9]
answer = Solution().sortedArrayToBST(nums)
print(answer)