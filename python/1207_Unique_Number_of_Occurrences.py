"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""
from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums_dict_values = Counter(arr).values()
        return len(set(nums_dict_values))==len(nums_dict_values)
        
        # nums_dict = {}

        # for num in arr:
        #     if num in nums_dict:
        #         nums_dict[num] += 1
        #     else:
        #         nums_dict[num] = 1
                
        # return len(nums_dict) == len(set(nums_dict.values()))
        
"""
Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""

print(Solution().uniqueOccurrences([1,2,2,1,1,3]))

print(Solution().uniqueOccurrences([1,2]))

print(Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
