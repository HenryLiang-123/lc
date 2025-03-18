// Last updated: 3/18/2025, 2:40:24 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def bfs():
            if not root:
                return []
            q = deque([root])
            result = []
            while q:
                level_size = len(q)
                level_elements = []
                for i in range(level_size):
                    node = q.popleft()
                    level_elements.append(node.val)
                    if node.left:
                        q.append(node.left)
                    
                    if node.right:
                        q.append(node.right)

                result.append(level_elements)
            
            return result

        return bfs()