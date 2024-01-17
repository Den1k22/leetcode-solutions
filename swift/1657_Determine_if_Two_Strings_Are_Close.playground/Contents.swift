"""
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Constraints:
1 <= word1.length, word2.length <= 10^5
word1 and word2 contain only lowercase English letters.
"""

class Solution {
    func closeStrings(_ word1: String, _ word2: String) -> Bool {
        let word1Hash = word1.reduce(into: [:]) { counts, element in
            counts[element, default: 0] += 1 }
        let word2Hash = word2.reduce(into: [:]) { counts, element in
            counts[element, default: 0] += 1 }

        let word1HashKeys = word1Hash.keys.sorted()
        let word2HashKeys = word2Hash.keys.sorted()
        let word1HashValues = word1Hash.values.sorted()
        let word2HashValues = word2Hash.values.sorted()

        return  word1HashKeys == word2HashKeys && word1HashValues == word2HashValues


//        var word1Hash = [Character: Int]()
//        var word2Hash = [Character: Int]()
//
//        for char in word1 {
//            if let charCount = word1Hash[char] {
//                word1Hash[char] = charCount + 1
//            } else {
//                word1Hash[char] = 1
//            }
//        }
//
//        for char in word2 {
//            if let charCount = word2Hash[char] {
//                word2Hash[char] = charCount + 1
//            } else {
//                word2Hash[char] = 1
//            }
//        }
//
//        let word1HashValues = word1Hash.values.sorted()
//        let word2HashValues = word2Hash.values.sorted()
//
//        let word1HashKeys = word1Hash.keys.sorted()
//        let word2HashKeys = word2Hash.keys.sorted()
//
//
//        return word1HashValues.elementsEqual(word2HashValues) && word1HashKeys.elementsEqual(word2HashKeys)
    }
}

"""
Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
"""

print(Solution().closeStrings("abc", "bca"))

print(Solution().closeStrings("a", "aa"))

print(Solution().closeStrings("cabbba", "abbccc"))

print(Solution().closeStrings("uau", "ssx"))
