# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def bfs(root):
            if not root:
                return []
            q = deque([root])
            direction = 1 # left to right
            traversal = []
            while q:
                level_size = len(q)
                level = []
                for i in range(level_size):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    
                    level.append(node.val)
                if direction == 1:
                    traversal.append(level)
                else:
                    traversal.append(level[::-1])
                direction *= -1
                
            return traversal

        return (bfs(root))
                        