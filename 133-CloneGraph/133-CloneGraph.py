// Last updated: 3/7/2025, 5:03:10 PM
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
        old_to_new = {}
        old_to_new2 = {}
        def bfs(root):
            if not root:
                return root 
            old_to_new[root] = Node(root.val, [])
            q = deque([root]) # old node
            while q:
                old_node = q.popleft()
                for nei in old_node.neighbors:
                    if nei not in old_to_new:
                        new_node = Node(nei.val, [])
                        old_to_new[nei] = new_node
                        q.append(nei)
                    else:
                        # print(old_node.val)
                        if old_to_new[old_node] not in old_to_new[nei].neighbors:
                            old_to_new[nei].neighbors.append(old_to_new[old_node])
                        if old_to_new[nei] not in old_to_new[old_node].neighbors:
                            old_to_new[old_node].neighbors.append(old_to_new[nei])

            return old_to_new[root]

        return (bfs(node))


                    


