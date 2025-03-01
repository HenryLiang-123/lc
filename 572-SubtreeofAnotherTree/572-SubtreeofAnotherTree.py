// Last updated: 3/1/2025, 3:31:22 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root1, root2):
            if root1 is None and root2 is None:
                return True

            if root1 is None or root2 is None:
                return False

            return root1.val == root2.val and isSame(root1.left, root2.left) and isSame(root1.right, root2.right)

        def dfs(root, subroot):
            if root is None or subroot is None:
                return root is None and subroot is None

            if isSame(root, subroot):
                return True
            else:
                return dfs(root.left, subroot) or dfs(root.right, subroot)

        return dfs(root, subRoot)