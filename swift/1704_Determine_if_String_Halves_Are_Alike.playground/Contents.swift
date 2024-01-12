"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

Constraints:
2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.
"""

class Solution {
    func halvesAreAlike(_ s: String) -> Bool {
        let vowels = Set("aeiouAEIOU")

        return s.prefix(s.count / 2).filter({ vowels.contains($0)}).count == s.suffix(s.count / 2).filter({ vowels.contains($0)}).count

//        let vowels = Set("aeiouAEIOU")
//        let firstHalf = s.prefix(s.count / 2)
//        let secondHalf = s.suffix(s.count / 2)
//
//        return firstHalf.filter({ vowels.contains($0)}).count == secondHalf.filter({ vowels.contains($0)}).count
    }
}

"""
Example 1:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

    Example 2:
Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
"""

print(Solution().halvesAreAlike("book"))

print(Solution().halvesAreAlike("textbook"))
