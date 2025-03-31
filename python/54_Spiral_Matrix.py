"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        total = m * n
        dirs = {
            "r": (0,1),
            "d": (1,0),
            "l": (0,-1),
            "u": (-1,0)
        }
        dir = dirs["r"]
        top = 0
        bottom = m - 1
        right = n - 1
        left = 0
        count = 0

        answer = []
        i,j = 0,0
        while True:
            answer.append(matrix[i][j])
            count += 1
            if dir == dirs["r"] and j == right:
                top += 1
                dir = dirs["d"]
            if dir == dirs["d"] and i == bottom:
                right -= 1
                dir = dirs["l"]
            if dir == dirs["l"] and j == left:
                bottom -= 1
                dir = dirs["u"]
            if dir == dirs["u"] and i == top:
                left += 1
                dir = dirs["r"]

            i += dir[0]
            j += dir[1]

            if total == count:
                break
            
        return answer
    
        # if not matrix:
        #     return []

        # rows, cols = len(matrix), len(matrix[0])
        # top, bottom, left, right = 0, rows-1, 0, cols-1
        # result = []
        
        # while len(result) < rows * cols:
        #     for i in range(left, right+1):
        #         result.append(matrix[top][i])
        #     top += 1
            
        #     for i in range(top, bottom+1):
        #         result.append(matrix[i][right])
        #     right -= 1
            
        #     if top <= bottom:
        #         for i in range(right, left-1, -1):
        #             result.append(matrix[bottom][i])
        #         bottom -= 1
            
        #     if left <= right:
        #         for i in range(bottom, top-1, -1):
        #             result.append(matrix[i][left])
        #         left += 1
        
        # return result

"""
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
print("[1,2,3,6,9,8,7,4,5]")
print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

print("[1,2,3,4,8,12,11,10,9,5,6,7]")
print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
