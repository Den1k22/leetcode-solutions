"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

Constraints:
1 <= path.length <= 10^4
path[i] is either 'N', 'S', 'E', or 'W'.
"""
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        current_x = 0
        current_y = 0
        points = {(current_x, current_y)}

        for c in path:
            if c == 'N':
                current_y += 1 
            elif c == 'S':
                current_y -= 1 
            elif c == 'E':
                current_x += 1
            else:
                current_x -= 1
            
            point = (current_x, current_y)

            if point in points:
                return True
            else:
                points.add(point)
            
        return False

"""
Example 1:
Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
"""

path = "NES"
print(Solution().isPathCrossing(path))

path = "NESWW"
print(Solution().isPathCrossing(path))
