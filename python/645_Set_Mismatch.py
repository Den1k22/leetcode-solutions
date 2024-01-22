"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Constraints:
2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4
"""
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        init_sum = len(nums)*(len(nums)+1)/2
        missing_num = int(init_sum - sum(set(nums)))
        duplicated_num = int(sum(nums) - init_sum + missing_num)
        return [duplicated_num, missing_num]

        # true_set = [i + 1 for i in range(len(nums))]
        # used_nums = {}
        
        # duplicate = 0
        # while (nums):        
        #     num = nums.pop()

        #     if num in used_nums:
        #         duplicate = num
        #     else:
        #         used_nums[num] = 1
            
        #     if num in true_set:
        #         true_set.remove(num)
            
        # return [duplicate, true_set[0]]
                
"""
Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]
"""

print(Solution().findErrorNums([1,2,2,4]))
print(Solution().findErrorNums([1,1]))
print(Solution().findErrorNums([3,2,2]))
print(Solution().findErrorNums([2,2]))