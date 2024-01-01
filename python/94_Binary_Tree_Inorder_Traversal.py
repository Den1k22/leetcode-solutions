"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        answer = []
        stack = [root]
        
        while stack:
            current_node = stack.pop()
            if not current_node:
                continue
            
            node_left = current_node.left
            node_right = current_node.right

            if node_left:
                current_node.left = None
                stack.append(current_node)
                stack.append(node_left)
                continue
            
            if node_right:
                answer.append(current_node.val)
                stack.append(node_right)
                continue
            
            answer.append(current_node.val)
        
        return answer
        
"""
Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
"""
test_root = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3, left=None, right=None), right=None))
test_root2 = TreeNode(val=1, left=None, right=None)

print(Solution().inorderTraversal(test_root))
