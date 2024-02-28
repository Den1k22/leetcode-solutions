"""
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Constraints:
0 <= left <= right <= 231 - 1
"""
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # if left == right:
        #     return left

        # bin_right = "{0:b}".format(right)
        # bin_left = "{0:b}".format(left)[0:].zfill(len(bin_right))
        
        # res = ""
        # for i in range(len(bin_right)):
        #     if (bin_right[i] != bin_left[i]):
        #         res += "0" * (len(bin_right) - i)
        #         break
        #     else:
        #         res += bin_right[i]
        
        # return int(res, 2)
        shift = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        
        return left << shift
        

"""
Example 1:
Input: left = 5, right = 7
Output: 4

Example 2:
Input: left = 0, right = 0
Output: 0

Example 3:
Input: left = 1, right = 2147483647
Output: 0
"""

print(Solution().rangeBitwiseAnd(5, 7))
print(Solution().rangeBitwiseAnd(0, 0))
print(Solution().rangeBitwiseAnd(1, 2147483647))
print(Solution().rangeBitwiseAnd(1, 1))
print(Solution().rangeBitwiseAnd(5, 5))

