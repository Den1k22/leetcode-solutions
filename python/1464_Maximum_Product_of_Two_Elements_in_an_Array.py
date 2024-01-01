"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 
Constraints:
2 <= nums.length <= 500
1 <= nums[i] <= 10^3
"""
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        i_max = i
        j_max = j

        while (i != j - 1):
            if (nums[j_max] < nums[i_max]):
                j -= 1
                if (nums[j] > nums[j_max]):
                    j_max = j
            else:
                i += 1
                if (nums[i] > nums[i_max]):
                    i_max = i

        return ((nums[i_max] - 1) * (nums[j_max] - 1))

"""
Example 1:
Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

Example 2:
Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

Example 3:
Input: nums = [3,7]
Output: 12
"""

nums = [3,4,5,2]
assert Solution().maxProduct(nums) == 12

nums = [1,5,4,5]
assert Solution().maxProduct(nums) == 16

nums = [3,7]
assert Solution().maxProduct(nums) == 12

