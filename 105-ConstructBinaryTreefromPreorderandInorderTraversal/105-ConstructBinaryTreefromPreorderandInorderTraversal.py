// Last updated: 2/18/2025, 10:59:42 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root_idx = 0
        n = len(inorder)
        node_to_idx = {inorder[i]:i for i in range(n)}

        def dfs(left, right):
            nonlocal root_idx
            if left > right:
                return None

            root = TreeNode(preorder[root_idx])
            root_idx += 1
            root_in_inorder = node_to_idx[root.val]
            root.left = dfs(left, root_in_inorder -1)
            root.right = dfs(root_in_inorder + 1, right)

            return root

        return dfs(0, n-1)


            