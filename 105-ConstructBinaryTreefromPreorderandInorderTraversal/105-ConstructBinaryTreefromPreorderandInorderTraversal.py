# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        num_to_index_inorder = {}
        for i, num in enumerate(inorder):
            num_to_index_inorder[num] = i

        root_index = 0
        def dfs(left, right):
            nonlocal root_index
            if left > right:
                return None
            print(root_index)
            root = TreeNode(preorder[root_index])
            split_index = num_to_index_inorder[root.val]
            root_index += 1

            root.left = dfs(left, split_index - 1)
            root.right = dfs(split_index + 1, right)

            return root

        return dfs(0, len(preorder)-1)

            
