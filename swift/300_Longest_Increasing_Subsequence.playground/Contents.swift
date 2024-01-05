"""
Given an integer array nums, return the length of the longest strictly increasing
subsequence

Constraints:
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4
"""

class Solution {
    func lengthOfLIS(_ nums: [Int]) -> Int {
        var longestSubNums = [nums[0]]

        for i in 1..<nums.count {
            if longestSubNums.last! < nums[i] {
                longestSubNums.append(nums[i])
            } else {
                let index = longestSubNums.firstIndex(where: {$0 >= nums[i]})
                longestSubNums[index!] = nums[i]
            }
        }

        return longestSubNums.count
    }
}

"""
Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))

print(Solution().lengthOfLIS([0,1,0,3,2,3]))

print(Solution().lengthOfLIS([7,7,7,7,7,7,7]))
