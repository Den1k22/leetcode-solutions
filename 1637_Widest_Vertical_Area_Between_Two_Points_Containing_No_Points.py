"""
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.

Constraints:
n == points.length
2 <= n <= 10^5
points[i].length == 2
0 <= xi, yi <= 10^9
"""
from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[0])

        max_diff = 0
        for i in range(1, len(sorted_points)):
            max_diff = max(max_diff, sorted_points[i][0] - sorted_points[i-1][0])

        return max_diff


"""
Example 1:
Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: Both the red and the blue area are optimal.

Example 2:
Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
Output: 3
"""

points = [[8,7],[9,9],[7,4],[9,7]]
print(Solution().maxWidthOfVerticalArea(points))

points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
print(Solution().maxWidthOfVerticalArea(points))
