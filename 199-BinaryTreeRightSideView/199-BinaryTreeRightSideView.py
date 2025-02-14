# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(node):
            q = deque([node])
            result = []
            while q:
                traversal = []
                n = len(q)
                # print(q)
                for i in range(n):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    
                    if node.right:
                        q.append(node.right)
                    
                    
                    traversal.append(node.val)
                result.append(traversal[-1])

            return result

        if not root:
            return []
        return (bfs(root))