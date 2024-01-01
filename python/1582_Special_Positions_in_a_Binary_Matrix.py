"""
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
"""
from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        answer = 0
        for i in range(m):
            sum_row = 0
            number_index = -1    

            for j in range(n):
                if (mat[i][j] == 1):
                    number_index = j
                    sum_row += mat[i][j]

            if (sum_row == 1):
                sum_column = 0
                for j in range(m):
                    sum_column += mat[j][number_index]
                
                if (sum_column == 1):
                    answer += 1

        return answer

"""
Example 1:
Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:
Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
"""

mat = [[1,0,0],[0,0,1],[1,0,0]]
assert Solution().numSpecial(mat) == 1

mat = [[1,0,0],[0,1,0],[0,0,1]]
assert Solution().numSpecial(mat) == 3

mat = [[0,0,0,1],[1,0,0,0],[0,1,1,0],[0,0,0,0]]
assert Solution().numSpecial(mat) == 2

mat = [[0,0,0,0,0],[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
assert Solution().numSpecial(mat) == 3

mat = [[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,1,0,0]]
assert Solution().numSpecial(mat) == 2


