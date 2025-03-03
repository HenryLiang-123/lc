# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            smaller = min(p.val, q.val)
            larger = max(p.val, q.val)
            while True:
                if root.val > larger:
                    root = root.left
                elif root.val < smaller:
                    root = root.right
                elif smaller <= root.val <= larger:
                    return root

        return dfs(root)
        