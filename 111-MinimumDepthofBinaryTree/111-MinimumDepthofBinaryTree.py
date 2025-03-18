// Last updated: 3/18/2025, 1:51:21 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0

            if not root.left:
                return 1 + dfs(root.right)
            elif not root.right:
                return 1 + dfs(root.left)
            else:
                left = dfs(root.left)
                right = dfs(root.right)
                return 1 + min(left, right)

        return dfs(root)