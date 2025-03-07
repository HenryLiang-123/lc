// Last updated: 3/6/2025, 8:51:29 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def bfs(root):
            q = deque([root])
            seen_none = False
            while q:
                node = q.popleft()
                

                if not node:
                    seen_none = True
                else:
                    if node.left is None and node.right is not None:
                        return False

                    if node and seen_none:
                        return False
                    # if node.left:
                    q.append(node.left)

                # if node.right:
                    q.append(node.right)                
                

                

            return True

        return bfs(root)
