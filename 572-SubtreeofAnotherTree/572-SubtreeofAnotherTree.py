// Last updated: 2/22/2025, 4:09:46 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(root1, root2):
            if root1 is None and root2 is None:
                return True

            if root1 is None or root2 is None:
                return False

            return root1.val == root2.val and check(root1.left, root2.left) and check(root1.right, root2.right)

        def dfs(root, subroot):
            if root is None and subroot is None:
                return True

            if root is None or subroot is None:
                return False

            if not check(root, subroot):
                return dfs(root.left, subroot) or dfs(root.right, subroot)

            return True

        return dfs(root, subRoot)

            