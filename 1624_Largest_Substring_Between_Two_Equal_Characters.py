"""
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

Constraints:
1 <= s.length <= 300
s contains only lowercase English letters.
"""

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)

        if n == 1:
            return -1

        if len(set(s)) == n:
            return -1
        
        letters_dict = {}
        for i in range(len(s)):
            if s[i] in letters_dict:
                letters_dict[s[i]].append(i)
            else:
                letters_dict[s[i]] = [i]

        m = 0
        for k in letters_dict.keys():
            letter_arr = letters_dict[k]
            if len(letter_arr) > 1:
                m = max(m, letters_dict[k][-1] - letters_dict[k][0] - 1)
                
        return m
    
        # Not my solution:
        # length = -1
        # myhash= {}
        # for i in range(len(s)):
        #     if s[i] not in myhash:
        #         myhash[s[i]] = i
        #     else:
        #         length = max(length , i- myhash.get(s[i]) -1)
        # return length

"""
Example 1:
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:
Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".

Example 3:
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
"""

s = "aa"
print(Solution().maxLengthBetweenEqualCharacters(s))

s = "abca"
print(Solution().maxLengthBetweenEqualCharacters(s))

s = "cbzxy"
print(Solution().maxLengthBetweenEqualCharacters(s))


