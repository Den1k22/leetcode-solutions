"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Constraints:
The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def getLeafs(root: Optional[TreeNode]):
            leafs = []
            stack = [root]

            while stack:
                current_node = stack.pop()
                if not current_node:
                    continue

                if (current_node.left == None and current_node.right == None):
                    leafs.append(current_node.val)
                    continue

                if current_node.right:
                    stack.append(current_node.right)

                if current_node.left:
                    stack.append(current_node.left)

            return leafs
        
        return getLeafs(root1) == getLeafs(root2)
        

"""
Example 1:
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
"""

test_root_1 = TreeNode(val=1, left=TreeNode(val=2), right=None)
test_root_2 = TreeNode(val=2, left=TreeNode(val=2), right=None)

print(Solution().leafSimilar(test_root_1, test_root_2))