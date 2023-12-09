"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Constraints:

1 <= m, n <= 100
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem_steps = []
        
        for i in range(m):
            temp = []
            for j in range(n):
                if (j == 0 or i == 0):
                    temp.append(1)
                else:
                    temp.append(mem_steps[i - 1][j] + temp[j - 1])
            mem_steps.append(temp)
            
        return (mem_steps[m - 1][n - 1])
                    
            


"""
Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""

print(Solution().uniquePaths(40, 50))