"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.

Constraints:
1 <= matches.length <= 10^5
matches[i].length == 2
1 <= winneri, loseri <= 10^5
winneri != loseri
All matches[i] are unique.
"""

class Solution {
    func findWinners(_ matches: [[Int]]) -> [[Int]] {
        var lossesHash: [Int: Int] = [:]

        for match in matches {
            lossesHash[match[0], default: 0] += 0
            lossesHash[match[1], default: 0] += 1
        }

        var zeroLosses: [Int] = []
        var oneLoss: [Int] = []
        for (player, losses) in lossesHash {
            if losses == 0 {
                zeroLosses.append(player)
            } else if losses == 1 {
                oneLoss.append(player)
            }
        }

        zeroLosses.sort()
        oneLoss.sort()

        return [zeroLosses, oneLoss]

//        var lossesArray = Array(repeating: 0, count: 100001)
//        for match in matches {
//            if lossesArray[match[0]] == 0 {
//                lossesArray[match[0]] = -1
//            }
//
//            if lossesArray[match[1]] == -1 {
//                lossesArray[match[1]] = 1
//            } else {
//                lossesArray[match[1]] += 1
//            }
//        }
//
//        var zeroLosses: [Int] = []
//        var oneLoss: [Int] = []
//
//        for i in 1..<100001 {
//            if lossesArray[i] == -1 {
//                zeroLosses.append(i)
//            } else if lossesArray[i] == 1 {
//                oneLoss.append(i)
//            }
//        }
//
//        return [zeroLosses, oneLoss]
    }
}

"""
Example 1:
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

Example 2:
Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
"""

print(Solution().findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))

print(Solution().findWinners([[2,3],[1,3],[5,4],[6,4]]))

