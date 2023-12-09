"""
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Constraints:

1 <= n <= 1000
"""

class Solution:
    def totalMoney(self, n: int) -> int:
        full_week = n // 7
        mod = n % 7
        return (28 * full_week) + (7 * (full_week - 1) * full_week // 2) + full_week * mod + mod * (mod + 1) // 2

        
        # first_week = [1, 2, 3, 4, 5, 6, 7]
        
        # if (n <= 7):
        #     return sum(first_week[:n])
        
        # total_weeks_count = n // 7
        # last_week = [total_weeks_count + i for i in range(7)]
        
        # total = (sum(first_week) + sum(last_week)) * total_weeks_count // 2
        
        # for i in range(n % 7):
        #     last_week[i] += 1
            
        # left_days = n % 7
        # if (left_days > 0):
        #     total += sum(last_week[:left_days])
            
        # return total

"""
Example 1:
Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Example 2:
Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.

Example 3: 
Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
 
"""

print(Solution().totalMoney(20))
