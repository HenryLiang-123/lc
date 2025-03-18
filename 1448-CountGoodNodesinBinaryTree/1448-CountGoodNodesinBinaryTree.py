// Last updated: 3/18/2025, 2:34:02 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, max_on_path):
            if not root:
                return 0

            result = 0

            if root.val >= max_on_path:
                result += 1

            max_on_path = max(max_on_path, root.val)

            left_count = dfs(root.left, max_on_path)
            right_count = dfs(root.right, max_on_path)

            return result + left_count + right_count

        return dfs(root, root.val)