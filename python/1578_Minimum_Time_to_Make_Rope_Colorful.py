"""
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.

Constraints:
n == colors.length == neededTime.length
1 <= n <= 10^5
1 <= neededTime[i] <= 10^4
colors contains only lowercase English letters.
"""
from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        current_colors_first_index = 0
        total_time = 0
        colors += '0'
        for i in range(1, len(colors)):
            if colors[current_colors_first_index] != colors[i]:
                if current_colors_first_index + 1 == i:
                    current_colors_first_index = i
                else:
                    total_time += sum(neededTime[current_colors_first_index: i]) - max(neededTime[current_colors_first_index: i])
                    current_colors_first_index = i
        
        return total_time
        

"""
Example 1:
Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.

Example 2:
Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.

Example 3:
Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2
Explanation: Bob will remove the ballons at indices 0 and 4. Each ballon takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
"""

colors = "abaac"
neededTime = [1,2,3,4,5]
print(Solution().minCost(colors, neededTime))

colors = "abc"
neededTime = [1,2,3]
print(Solution().minCost(colors, neededTime))

colors = "aabaa"
neededTime = [1,2,3,4,1]
print(Solution().minCost(colors, neededTime))
