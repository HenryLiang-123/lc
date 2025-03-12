// Last updated: 3/12/2025, 5:07:07 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return None

            if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
                return root
            elif p.val <= root.val and q.val <= root.val:
                return dfs(root.left)
            else:
                return dfs(root.right)

        return dfs(root)