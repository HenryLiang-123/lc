// Last updated: 3/9/2025, 10:38:32 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(root):
            if not root:
                return root

            if root in old_to_new:
                return old_to_new[root]

            new_node = Node(root.val, [])
            old_to_new[root] = new_node
            for nei in root.neighbors:
                new_node.neighbors.append(dfs(nei))

            return new_node

        return dfs(node)
        