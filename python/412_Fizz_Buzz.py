"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Constraints:
1 <= n <= 104
"""
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [str(x + 1) for x in range(n)]

        for i in range(2, n, 3):
            answer[i] = "Fizz"

        for i in range(4, n, 5):
            answer[i] = "Buzz"

        for i in range(14, n, 15):
            answer[i] = "FizzBuzz"

        return answer
    
        # answer = []
        # for i in range (1, n + 1):
        #     if (i % 15 == 0):
        #         answer.append("FizzBuzz")
        #     elif(i % 3 == 0):
        #         answer.append("Fizz")
        #     elif(i % 5 == 0):
        #         answer.append("Buzz")
        #     else:
        #         answer.append(str(i))
        # return answer

"""
Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
"""


print(Solution().fizzBuzz(15))
