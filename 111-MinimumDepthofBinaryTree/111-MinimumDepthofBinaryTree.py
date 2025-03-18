# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        result = float('inf')
        def dfs(root):
            nonlocal result
            if not root:
                return 0

            if not root.left:
                return 1 + dfs(root.right)
            elif not root.right:
                return 1 + dfs(root.left)
            else:
                left_depth = dfs(root.left)
                right_depth = dfs(root.right)
                return min(left_depth, right_depth) + 1


        result = dfs(root)

        return result

            