"""
You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

Constraints:
The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 10^5
Each node has a unique value.
A node with a value of start exists in the tree.
"""
from typing import Optional
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        
        stack = [(root, None)]
        while stack: 
            node, prevNode = stack.pop()
            if prevNode: 
                graph[prevNode.val].append(node.val)
                graph[node.val].append(prevNode.val)
            if node.left: stack.append((node.left, node))
            if node.right: stack.append((node.right, node))
        
        ans = -1
        seen = {start}
        queue = deque([start])
        while queue: 
            for _ in range(len(queue)): 
                node = queue.popleft()
                for val in graph[node]: 
                    if val not in seen: 
                        seen.add(val)
                        queue.append(val)
            ans += 1
        return ans 

"""
Example 1:
Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.

Example 2:
Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.
"""

tree_1 = TreeNode(val=1, left=TreeNode(val=5, right=TreeNode(val=4, left=TreeNode(val=9), right=TreeNode(val=2))), right=TreeNode(val=3, left=TreeNode(val=10), right=TreeNode(val=6)))
print(Solution().amountOfTime(tree_1, 3))

tree_2 = TreeNode(val=1)
print(Solution().amountOfTime(tree_2, 1))