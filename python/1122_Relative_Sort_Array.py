"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

Constraints:

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.
"""
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # all_numbers = {x: 0 for x in arr2}
        # not_included = []
        
        # for num in arr1:
        #     if (num in all_numbers):
        #         all_numbers[num] += 1
        #     else:
        #         not_included.append(num)
        # not_included.sort()
        
        # answer = []
        # for num in arr2:
        #     answer += [num for _ in range(all_numbers[num])]
            
        # return answer + not_included
        
        max_element = max(arr1)
        all_numbers = [0] * (max_element + 1)
        
        for element in arr1:
            all_numbers[element] += 1
            
        result = []
        for num in arr2:
            while all_numbers[num] > 0:
                result.append(num)
                all_numbers[num] -= 1
                
        for num in range(max_element + 1):
            while all_numbers[num] > 0:
                result.append(num)
                all_numbers[num] -= 1
                
        return result

"""
Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Example 2:
Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
"""

print(Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
print(Solution().relativeSortArray([28,6,22,8,44,17],[22,28,8,6]))
