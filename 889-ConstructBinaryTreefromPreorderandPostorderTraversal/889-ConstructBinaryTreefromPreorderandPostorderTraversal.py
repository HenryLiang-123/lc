// Last updated: 2/28/2025, 8:28:36 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)
        mapping = {postorder[i]:i for i in range(n)}
        def dfs(pre_i, pre_j, post_i, post_j):
            
            if pre_i > pre_j or post_i > post_j:
                return None
            # print(pre_i)
            root = TreeNode(preorder[pre_i])
            if pre_i + 1 <= pre_j:
                next_node = preorder[pre_i + 1]
                node_in_post = mapping[next_node]
                length = node_in_post - post_i + 1
                root.left = dfs(pre_i+1, pre_i + length, post_i, node_in_post)
                root.right = dfs(pre_i + length + 1, pre_j, node_in_post+1, post_j-1)

            return root

        return dfs(0,n-1, 0, n-1)