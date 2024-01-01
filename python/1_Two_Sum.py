
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        savedResults = {}
        
        for i in range(len(nums)):
            requiredNumber = target - nums[i]
            if (requiredNumber in savedResults):
                return [savedResults[requiredNumber], i]
            else:
                savedResults[nums[i]] = i
            
nums = [-1,-2,-3,-4,-5]
target = -8

res = Solution().twoSum(nums, target)
print(res)