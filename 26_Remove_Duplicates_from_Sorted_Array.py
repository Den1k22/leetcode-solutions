from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq_numbers_count = 1
        for i in range(1, len(nums)):
            current = nums[i]
            prev_number = nums[i - 1]
            if current > prev_number:
                nums[uniq_numbers_count] = current
                uniq_numbers_count += 1
                
        return uniq_numbers_count

nums = [0,0,1,1,1,2,2,3,3,4]

res = Solution().removeDuplicates(nums)
print(nums)
print(res)