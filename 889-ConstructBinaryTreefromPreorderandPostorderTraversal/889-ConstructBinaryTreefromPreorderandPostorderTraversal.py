# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        post_node_to_idx = {postorder[i]:i for i in range(n)}
        idx = 0
        def dfs(left_pre, right_pre, left_post, right_post):
            if left_pre > right_pre or left_post > right_post:
                return None

            root = TreeNode(preorder[left_pre])
            if left_pre != right_pre:
                left_node = preorder[left_pre + 1]
                left_size = post_node_to_idx[left_node] - left_post + 1

                root.left = dfs(left_pre + 1, left_pre + left_size, left_post, post_node_to_idx[left_node])
                root.right = dfs(left_pre + left_size + 1, right_pre, post_node_to_idx[left_node] + 1, right_post - 1)

            return root

        return dfs(0, n-1, 0, n-1)


            

        