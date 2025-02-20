# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0

            max_depth = float('-inf')
            
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            max_depth = max(left_depth, right_depth) + 1

            return max_depth

        return dfs(root) 
            