"""
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Constraints:

The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 9
"""
from typing import Optional
from typing import List

from collections import Counter

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        result = 0
        
        stack = [(root, 0) ]
        while stack:
            node, path = stack.pop()
            if node is not None:
                # compute occurences of each digit 
                # in the corresponding register
                path = path ^ (1 << node.val)
                # if it's a leaf, check if the path is pseudo-palindromic
                if node.left is None and node.right is None:
                    # check if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        result += 1
                else:
                    stack.append((node.right, path))
                    stack.append((node.left, path))
        
        return result
        
        # def isPalindrom(current_values: str):
        #     current_values_dict_values = Counter(current_values).values()
        #     one_uniq = 0
            
        #     for val in current_values_dict_values:
        #         if val % 2 == 1:
        #             one_uniq += 1
        #             if one_uniq > 1:
        #                 return False
            
        #     return True
        
        # def getPalindrom(root : Optional[TreeNode], current_values: str):
        #     if root == None:
        #         return 0
            
        #     current_values += str(root.val)
            
        #     if (root.left == None and root.right == None):
        #         if (isPalindrom(current_values)):
        #             return 1
        #         else:
        #             return 0
            
        #     return getPalindrom(root.left, current_values[:]) + getPalindrom(root.right, current_values[:])
        
        # return getPalindrom(root, [])

                

"""
Example 1:
Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:
Input: root = [9]
Output: 1
"""

test_root1 = TreeNode(val=2, left=TreeNode(val=3, left=TreeNode(val=3, left=None, right=None), right=TreeNode(val=1, left=None, right=None)), right=TreeNode(val=1, left=None, right=TreeNode(val=1, left=None, right=None)))
print(Solution().pseudoPalindromicPaths(test_root1))

test_root2 = TreeNode(val=2, left=TreeNode(val=1, left=TreeNode(val=1, left=None, right=None), right=TreeNode(val=3, left=None, right=TreeNode(val=1, left=None, right=None))), right=TreeNode(val=1, left=None, right=None))
print(Solution().pseudoPalindromicPaths(test_root2))

test_root3 = TreeNode(val=9, left=None, right=None)
print(Solution().pseudoPalindromicPaths(test_root3))