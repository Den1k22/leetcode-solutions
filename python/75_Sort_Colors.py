"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
"""
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        right = len(nums) - 1
        left = 0

        while (nums[right] == 2 and right != left):
            right -= 1

        curr = left

        while (curr <= right):
            if (curr == left and nums[curr] == 0):
                left += 1
                curr += 1

            elif (nums[curr] == 0 and curr != left):
                nums[curr] = nums[left]
                nums[left] = 0
                left += 1

            elif (nums[curr] == 2):
                nums[curr] = nums[right]
                nums[right] = 2
                right -= 1

            else:
                curr += 1

"""
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
"""
