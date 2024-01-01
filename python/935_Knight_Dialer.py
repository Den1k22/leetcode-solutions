"""
The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L).
The possible movements of chess knight are shown in this diagaram:

We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).


Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 109 + 7.

Constraints:

1 <= n <= 5000
"""

class Solution:
    def knightDialer(self, n: int) -> int:
        if (n == 1):
            return 10
        
        MOD = 10**9 + 7
        
        total_per_number = [1] * 10
        total_per_number[5] = 0
        
        for _ in range(1, n):
            temp_per_number = [0] * 10
            
            temp_per_number[0] = (total_per_number[4] + total_per_number[6]) % MOD
            temp_per_number[1] = (total_per_number[6] + total_per_number[8]) % MOD
            temp_per_number[2] = (total_per_number[7] + total_per_number[9]) % MOD
            temp_per_number[3] = (total_per_number[4] + total_per_number[8]) % MOD
            temp_per_number[4] = (total_per_number[3] + total_per_number[9] + total_per_number[0]) % MOD
            temp_per_number[6] = (total_per_number[1] + total_per_number[7] + total_per_number[0]) % MOD
            temp_per_number[7] = (total_per_number[2] + total_per_number[6]) % MOD
            temp_per_number[8] = (total_per_number[1] + total_per_number[3]) % MOD
            temp_per_number[9] = (total_per_number[2] + total_per_number[4]) % MOD
            
            total_per_number = temp_per_number
            
        return sum(total_per_number) % MOD
        

print(Solution().knightDialer(3131))

"""
Example 1:
Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.

Example 2:
Input: n = 2
Output: 20
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]

Example 3:
Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.
"""