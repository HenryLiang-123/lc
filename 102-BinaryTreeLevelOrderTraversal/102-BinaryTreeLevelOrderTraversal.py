# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        def bfs(node):
            q = deque([node])
            while q:
                curr_level = len(q)
                curr_nodes = []
                for i in range(curr_level):
                    curr = q.popleft()
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)

                    curr_nodes.append(curr.val)

                result.append(curr_nodes)
        bfs(root)
        return result



