# Last updated: 4/4/2025, 4:16:32 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # find nodes where depths are the same on both sides
        # root_to_depth = {}
        def dfs(root, curr_depth):
            if not root:
                return None, curr_depth + 1

            left_node, left_depth = dfs(root.left, curr_depth+1)
            right_node, right_depth = dfs(root.right, curr_depth+1)

            if left_depth > right_depth:
                return left_node, left_depth
            elif left_depth < right_depth:
                return right_node, right_depth
            else:
                return root, left_depth
        

        return dfs(root, 0)[0]