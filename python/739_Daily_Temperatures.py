"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Constraints:
1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
"""
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        res = [0] * size
        max_temp = 0

        for curr in range(size - 1, -1, -1):
            if temperatures[curr] >= max_temp:
                max_temp = temperatures[curr]
            else:
                days_counter = 1
                while(temperatures[curr + days_counter] <= temperatures[curr]):
                    days_counter += res[curr + days_counter]
                res[curr] = days_counter

        return res
        # size = len(temperatures)
        # res = [0 for _ in range(size)]
        # max_temp = temperatures[-1]

        # counter = len(temperatures) - 2
        # while counter >= 0:
        #     if temperatures[counter] > max_temp:
        #         res[counter] = 0
        #         max_temp = temperatures[counter]
        #     else:
        #         days_counter = 1
        #         for i in range(counter + 1, size):
        #             if temperatures[counter] < temperatures[i]:
        #                 res[counter] = days_counter
        #                 break
        #             else:
        #                 days_counter += 1

        #     counter -= 1

        # return res

"""
Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
print(Solution().dailyTemperatures([30,40,50,60]))
print(Solution().dailyTemperatures([30,60,90]))
