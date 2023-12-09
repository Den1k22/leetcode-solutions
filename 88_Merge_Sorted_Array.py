"""

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_index = m - 1
        nums2_index = n - 1
        total_index = m + n - 1
        
        while (total_index >= 0):
            if (nums1_index >= 0 and nums2_index >= 0):
                if (nums1[nums1_index] > nums2[nums2_index]):
                    nums1[total_index] = nums1[nums1_index]
                    nums1_index -= 1
                else:
                    nums1[total_index] = nums2[nums2_index]
                    nums2_index -= 1
            elif (nums1_index >= 0):
                nums1[total_index] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[total_index] = nums2[nums2_index]
                nums2_index -= 1
            total_index -= 1
        
        # if (n == 0):
        #     return
        
        # if (m == 0):
        #     for i in range(n):
        #         nums1[i] = nums2[i]
        #     return
        
        # temp_array = []
            
        # counter_1 = 0
        # counter_2 = 0
        # while (counter_1 < m):
        #     if (counter_2 < n):
        #         if (nums1[counter_1] <= nums2[counter_2]):
        #             if (len(temp_array) > 0):
        #                 if (nums1[counter_1] > temp_array[0]):
        #                     temp_array.append(nums1[counter_1])
        #                     nums1[counter_1] = temp_array.pop(0)
        #             counter_1 += 1     
        #         else:
        #             if (len(temp_array) > 0):
        #                 if (nums2[counter_2] >= temp_array[0]):
        #                     temp_array.append(nums1[counter_1])
        #                     nums1[counter_1] = temp_array.pop(0)
        #                     counter_1 += 1
        #                     continue
                    
        #             temp_array.append(nums1[counter_1])
        #             nums1[counter_1] = nums2[counter_2]
        #             counter_1 += 1
        #             counter_2 += 1
        #     else:
        #         if (nums1[counter_1] > temp_array[0]):
        #                 temp_array.append(nums1[counter_1])
        #                 nums1[counter_1] = temp_array.pop(0)
        #         counter_1 += 1
                
        # while (counter_2 < n):
        #     if (len(temp_array) > 0):
        #         if (nums2[counter_2] >= temp_array[0]):
        #             nums1[counter_1] = temp_array.pop(0)
        #             counter_1 += 1
        #             continue

        #     nums1[counter_1] = nums2[counter_2]
        #     counter_1 += 1
        #     counter_2 += 1
        
        # while (counter_1 < m + n):
        #     if (len(temp_array) > 0):
        #         nums1[counter_1] = temp_array.pop(0)
        #     counter_1 += 1

nums1 = [1,2,4,5,6,0]
m = 5
nums2 = [3]
n = 1

Solution().merge(nums1, m, nums2, n)
print(nums1)

"""
Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 
"""