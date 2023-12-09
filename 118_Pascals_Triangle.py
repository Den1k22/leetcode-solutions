"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Constraints:

1 <= numRows <= 30
"""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        
        if (numRows == 1):
            return answer
        
        for row in range(1, numRows):
            temp_list = []
            for column in range(row + 1):
                if (column == 0):
                    temp_list.append(1)
                elif (column == row):
                    temp_list.append(1)
                else:
                    temp_list.append(answer[row - 1][column - 1] + answer[row - 1][column])
                    
            answer.append(temp_list)
            
        return answer

"""
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
"""

print(Solution().generate(6))