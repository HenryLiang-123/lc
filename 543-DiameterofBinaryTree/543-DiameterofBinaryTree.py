// Last updated: 2/17/2025, 2:51:42 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(root):
            nonlocal result
            if not root:
                return 0

            left_len = dfs(root.left)
            right_len = dfs(root.right)

            result = max(result, left_len + right_len)

            return max(left_len, right_len) + 1

        dfs(root)
        return result