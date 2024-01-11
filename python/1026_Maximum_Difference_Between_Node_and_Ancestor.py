"""
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

Constraints:
The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 10^5
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        def depthFirstSearch(root, curMin, curMax):
            if root:
                self.answer = max(self.answer, root.val - curMin, curMax - root.val)
                curMin, curMax = min(curMin, root.val), max(curMax, root.val)
                depthFirstSearch(root.left, curMin, curMax)
                depthFirstSearch(root.right, curMin, curMax)

        depthFirstSearch(root, root.val, root.val)
        return self.answer

"""
Example 1:
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Example 2:
Input: root = [1,null,2,null,0,3]
Output: 3
"""

tree_1 = TreeNode(val=8, left=TreeNode(val=3, left=TreeNode(val=1), right=TreeNode(val=6, left=TreeNode(val=4), right=TreeNode(val=7))), right=TreeNode(val=10, right=TreeNode(val=14, left=TreeNode(val=13))))
print(Solution().maxAncestorDiff(tree_1))

tree_2 = TreeNode(val=1, right=TreeNode(val=2, right=TreeNode(val=0, left=TreeNode(val=3))))
print(Solution().maxAncestorDiff(tree_2))

