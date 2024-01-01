from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        remained_numbers_count = 0
        for i in range(len(nums)):
            if (nums[i] != val):
                nums[remained_numbers_count] = nums[i]
                remained_numbers_count += 1
        return remained_numbers_count
    

nums = [0,1,2,2,3,0,4,2]
res = Solution().removeElement(nums, 2)
print(nums)
print(res)