"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root.left == root.right == None:
            return 0
        
        # store maximum diameter in TreeNode's val

        def diameterOfBinaryTreeCountMax(root: Optional[TreeNode]):
            if (root == None):
                return 0

            if (root.left == root.right == None):
                root.val = 1
                return 1

            left = diameterOfBinaryTreeCountMax(root.left)
            right = diameterOfBinaryTreeCountMax(root.right)

            if (root.left == None):
                root.val = max(right, root.right.val)
            elif (root.right == None):
                root.val = max(left, root.left.val)
            else:
                root.val = max(left + right, root.left.val, root.right.val)
            
            return 1 + max(left, right)

        diameterOfBinaryTreeCountMax(root)

        return root.val
    
    
        # Example solution
        
        # diameter = 0
        # def longest_path(node):
        #     if not node:
        #         return 0
        #     nonlocal diameter
        #     # recursively find the longest path in
        #     # both left child and right child
        #     left_path = longest_path(node.left)
        #     right_path = longest_path(node.right)

        #     # update the diameter if left_path plus right_path is larger
        #     diameter = max(diameter, left_path + right_path)

        #     # return the longest one between left_path and right_path;
        #     # remember to add 1 for the path connecting the node and its parent
        #     return max(left_path, right_path) + 1

        # longest_path(root)
        # return diameter

"""
Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
"""
