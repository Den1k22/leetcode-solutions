"""
You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.

Constraints:
1 <= n <= 104
"""

class Solution:
    def countLargestGroup(self, n: int) -> int:
        counts = [0] * 37
        for num in range(1, n+1):
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num = num // 10
            counts[digit_sum] += 1

        return counts.count(max(counts))

        # counts = [0 for _ in range(36)]
        # for num in range(1, n+1):
        #     digit_sum = 0
        #     while num > 0:
        #         left  = num % 10
        #         digit_sum += left
        #         num = num // 10
        #     counts[digit_sum - 1] += 1
        # m = max(counts)
        # return counts.count(m)

"""
Example 1:
Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.

Example 2:
Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
"""
