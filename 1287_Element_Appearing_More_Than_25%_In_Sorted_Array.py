"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Constraints:
1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
"""
from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quater_size = len(arr) // 4
        
        for i in range(len(arr) - quater_size):
            if (arr[i] == arr[i + quater_size]):
                return arr[i]
        
        # size = len(arr)
        # quater_size = size / 4
        
        # count = 1
        # element = arr[0]
        # element_count = 1
        # while count < size:
        #     if element_count > quater_size:
        #         return element
            
        #     next_element = arr[count]
            
        #     if (next_element == element):
        #         element_count += 1
        #     else:
        #         element = next_element
        #         element_count = 1
            
        #     count+= 1
            
        # return element

"""
Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:
Input: arr = [1,1]
Output: 1
"""

arr = [1,2,2,6,6,6,6,7,10]
print(Solution().findSpecialInteger(arr))

arr = [1,1]
print(Solution().findSpecialInteger(arr))
