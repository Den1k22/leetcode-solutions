"""
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Constraints:
1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
"""
from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        nums_dict_values = list(Counter(arr).values())
        nums_dict_values.sort()
        size = len(nums_dict_values)
        
        i = 0
        while i < size:
            k -= nums_dict_values[i]
            if k < 0:
                break
            i += 1

        return size - i
"""
Example 1:
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
"""

print(Solution().findLeastNumOfUniqueInts([5,5,4], 1))
print(Solution().findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))