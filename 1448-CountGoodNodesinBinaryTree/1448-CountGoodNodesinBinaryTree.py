// Last updated: 3/18/2025, 12:28:55 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, path_max):

            if not root:
                return 0

            result = 0

            if root.val >= path_max:
                result += 1
                path_max = root.val

            left = dfs(root.left, path_max)
            right = dfs(root.right, path_max)

            return result + left + right

        return dfs(root, root.val)

            

            

            