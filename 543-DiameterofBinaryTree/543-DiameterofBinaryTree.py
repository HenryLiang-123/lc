// Last updated: 2/22/2025, 4:00:43 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')
        def dfs(root):
            nonlocal result
            if not root:
                return 0

            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            result = max(result, left_depth + right_depth)

            return max(left_depth, right_depth) + 1

        dfs(root)
        return result


            