# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        result = 0
        max_left = 0
        max_right = 0

        def dfs(root, path_len):
            nonlocal result
            if not root:
                return 0
            
            left_length = dfs(root.left, path_len+1)
            right_length = dfs(root.right, path_len+1)

            result = max(left_length+right_length, result)

            return max(left_length, right_length) + 1

            # print(root.val, left_length, right_length)


        dfs(root, 0)
        return result

            


