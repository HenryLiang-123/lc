// Last updated: 2/22/2025, 3:53:14 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')

        def dfs(root):
            nonlocal result
            if not root:
                return 0

            left_value = max(dfs(root.left), 0)
            right_value = max(dfs(root.right), 0)

            result = max(result, left_value + right_value + root.val)

            return max(left_value, right_value) + root.val

        dfs(root)
        
        return result