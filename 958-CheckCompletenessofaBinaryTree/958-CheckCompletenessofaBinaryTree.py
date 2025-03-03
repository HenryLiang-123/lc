// Last updated: 3/3/2025, 4:58:25 PM
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
            seen_null = False
            while q:
                node = q.popleft()
                if node.right and not node.left:
                    return False
                if seen_null and (node.left or node.right):
                    return False

                if node.left:
                    q.append(node.left)
                else:
                    seen_null = True

                if node.right:
                    q.append(node.right)
                else:
                    seen_null = True

            return True

        return bfs(root)
