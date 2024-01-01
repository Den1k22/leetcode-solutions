"""
You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""
from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        all_letters = "".join(words)
        uniq_letters = set(all_letters)

        words_count = len(words)

        for uniq_letter in uniq_letters:
            if all_letters.count(uniq_letter) % words_count != 0:
                return False
        
        return True

        # letter_hash = {}

        # for word in words:
        #     for letter in word:
        #         if letter in letter_hash:
        #             letter_hash[letter] += 1
        #         else:
        #             letter_hash[letter] = 1

        # total_words_count = len(words)
        # for hash_key in letter_hash.keys():
        #     if letter_hash[hash_key] % total_words_count != 0:
        #         return False
        
        # return True
"""
Example 1:
Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.

Example 2:
Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.
"""

words = ["abc","aabc","bc"]
print(Solution().makeEqual(words))
