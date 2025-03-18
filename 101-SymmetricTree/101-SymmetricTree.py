// Last updated: 3/18/2025, 2:04:47 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # old_root = root.copy()
        def copy_tree(node):
            if not node:
                return None

            new_node = TreeNode(node.val)
            new_node.left = copy_tree(node.left)
            new_node.right = copy_tree(node.right)

            return new_node

        old_root = copy_tree(root)
            
        def invert(node):
            if not node:
                return None
            
            node.right, node.left = invert(node.left), invert(node.right)

            return node

        def is_same(root1, root2):
            if root1 is None and root2 is None:
                return True
            
            if root1 is None or root2 is None:
                return False

            if root1.val == root2.val:
                return is_same(root1.left, root2.left) and is_same(root1.right, root2.right)
            
            return False

        inverted = invert(root)

        return is_same(inverted, old_root)