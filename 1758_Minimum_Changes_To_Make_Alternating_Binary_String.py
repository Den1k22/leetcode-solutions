"""
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

Constraints:
1 <= s.length <= 10^4
s[i] is either '0' or '1'.
"""

class Solution:
    def minOperations(self, s: str) -> int:
        starts_with_zero_counter = 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '1':
                    starts_with_zero_counter += 1
            else:
                if s[i] == '0':
                    starts_with_zero_counter += 1
        
        return min(starts_with_zero_counter, len(s) - starts_with_zero_counter)

"""
Example 1:
Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.

Example 2:
Input: s = "10"
Output: 0
Explanation: s is already alternating.

Example 3:
Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".
"""
s = "0100"
print(Solution().minOperations(s))
s = "10"
print(Solution().minOperations(s))
s = "1111"
print(Solution().minOperations(s))
s = "10010100"
print(Solution().minOperations(s))


