// Last updated: 3/7/2025, 5:14:37 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        def dfs(root):
            if not root:
                return root

            if root in seen:
                return seen[root]

            new_node = Node(root.val, [])
            seen[root] = new_node
            for nei in root.neighbors:
                new_node.neighbors.append(dfs(nei))
                
            
            return new_node

        return dfs(node)
        # def bfs(root):
        #     if not root:
        #         return root 
        #     old_to_new[root] = Node(root.val, [])
        #     q = deque([root]) # old node
        #     while q:
        #         old_node = q.popleft()
        #         for nei in old_node.neighbors:
        #             if nei not in old_to_new:
        #                 new_node = Node(nei.val, [])
        #                 old_to_new[nei] = new_node
        #                 q.append(nei)
        #             old_to_new[old_node].neighbors.append(old_to_new[nei])  

        #     return old_to_new[root]

        # return (bfs(node))


                    


