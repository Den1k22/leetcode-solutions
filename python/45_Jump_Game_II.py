"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = 0
        r = 0
        while r < len(nums) - 1:
            r_new = 0
            for i in range(l, r + 1):
                r_new = max(r_new, nums[i] + i)
            l = r + 1
            r = r_new 
            jumps += 1
            
        return jumps

        # n = len(nums)
        # nums[-1] = 0
        # i = n - 2
        # while i >= 0:
        #     if nums[i] == 0:
        #         nums[i] = nums[i+1] + 1
        #     else:
        #         nums[i] = min(nums[i + 1:i + 1+nums[i]]) + 1
        #     i -= 1
        # return nums[0]

"""
Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
"""

nums = [2,3,1,1,4]
print(Solution().jump(nums))

nums = [2,3,0,1,4]
print(Solution().jump(nums))
