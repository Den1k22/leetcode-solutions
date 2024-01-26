"""
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

Constraints:
1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n
"""
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        
        dp = [[ 0 for i in range(n)] for j in range(m)]
        dp[startRow][startColumn] = 1
        
        count = 0
        
        for _ in range(maxMove):
            temp = [[ 0 for i in range(n)] for j in range(m)]
            
            for i in range(m):
                for j in range(n):
                    if (i == m - 1):
                        count = (count + dp[i][j])
                        
                    if (j == n - 1):
                        count = (count + dp[i][j])
                        
                    if (i == 0):
                        count = (count + dp[i][j])
                        
                    if (j == 0):
                        count = (count + dp[i][j])
                        
                    temp[i][j] = (((dp[i - 1][j] if i > 0 else 0) + (dp[i + 1][j] if i < m - 1 else 0)) + ((dp[i][j - 1] if j > 0 else 0) + (dp[i][j + 1] if j < n - 1 else 0)))
                    
            dp = temp
        
        return count % MOD
        

"""
Example 1:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
"""

print(Solution().findPaths(2,2,2,0,0))

print(Solution().findPaths(1,3,3,0,1))
