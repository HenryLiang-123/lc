# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root_to_index = {}
        for i, val in enumerate(inorder):
            root_to_index[val] = i

        root_index = 0
        def dfs(left, right):
            nonlocal root_index

            if left > right:
                return None

            root = TreeNode(preorder[root_index])
            pivot = root_to_index[root.val]

            root_index += 1

            root.left = dfs(left, pivot - 1)
            root.right = dfs(pivot + 1, right)

            return root

        return dfs(0, len(preorder) - 1)