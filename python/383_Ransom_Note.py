"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Constraints:
1 <= ransomNote.length, magazine.length <= 10^5
ransomNote and magazine consist of lowercase English letters.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_hash = {}
        for letter in magazine:
            if letter in magazine_hash:
                magazine_hash[letter] += 1
            else:
                magazine_hash[letter] = 1

        for letter in ransomNote:
            if (letter not in magazine_hash):
                return False
            
            if (magazine_hash[letter] == 0):
                return False
            
            magazine_hash[letter] -= 1
            
        return True
            

"""
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

print(Solution().canConstruct("aa", "aab"))
