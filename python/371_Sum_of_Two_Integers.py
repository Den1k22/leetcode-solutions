"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Constraints:
-1000 <= a, b <= 1000
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xfff # 4095 because max sum is 2000 and one bit for minus sign
        while b:
            xor = (a^b) & mask
            carry = ((a&b)<<1) & mask
            a = xor
            b = carry

        if (a>>11) & 1:
            return a | ~mask
        return a

"""
Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5
"""
