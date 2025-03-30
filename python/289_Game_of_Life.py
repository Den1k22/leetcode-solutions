"""
ccording to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 
Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
"""
from typing import List
import copy

class Solution:
    def get_neighbors_count(self, x: int, y: int, board: List[List[int]], n: int, m: int) -> int:
        res = 0
        if x > 0:
            res += board[y][x-1]
        if x < n - 1:
            res += board[y][x+1]
        if y > 0:
            res += board[y-1][ x ]
        if y < m - 1:
            res += board[y+1][ x ]
        if x > 0 and y > 0:
            res += board[y-1][x-1]
        if x > 0 and y < m - 1:
            res += board[y+1][x-1]
        if x < n - 1 and y > 0:
            res += board[y-1][x+1]
        if x < n - 1 and y < m - 1:
            res += board[y+1][x+1]
        return res

    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        original = copy.deepcopy(board)

        for i in range(m):
            for j in range(n):
                count = self.get_neighbors_count(j, i, original, n, m)
                print(count)
                if count > 3 or count < 2:
                    board[i][j] = 0
                elif (count == 3):
                    board[i][j] = 1
        
"""
Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
"""

field = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Solution().gameOfLife(field)
print(field)
