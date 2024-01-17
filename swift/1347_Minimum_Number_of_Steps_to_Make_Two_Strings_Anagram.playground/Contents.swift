"""
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Constraints:

1 <= s.length <= 5 * 10^4
s.length == t.length
s and t consist of lowercase English letters only.
"""

class Solution {
    func minSteps(_ s: String, _ t: String) -> Int {
        var tHash = [Character: Int]()

        for char in t {
            if let charCount = tHash[char] {
                tHash[char] = charCount + 1
            } else {
                tHash[char] = 1
            }
        }

        var lettersForReplace = 0
        for char in s {
            if let charCount = tHash[char] {
                if charCount > 0 {
                    tHash[char] = charCount - 1
                } else {
                    lettersForReplace += 1
                }

            } else {
                lettersForReplace += 1
            }
        }

        return lettersForReplace
    }
}

"""
Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams.
"""

print(Solution().minSteps("bab", "aba"))

print(Solution().minSteps("leetcode", "practice"))

print(Solution().minSteps("anagram", "mangaar"))
