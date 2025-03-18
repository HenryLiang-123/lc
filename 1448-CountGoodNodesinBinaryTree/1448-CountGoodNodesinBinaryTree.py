// Last updated: 3/18/2025, 12:28:07 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, prev_max):

            if node is None:
                return 0
            
            if prev_max > node.val:
                count = 0
            else:
                count = 1

            prev_max = max(prev_max, node.val)
            # count = 1
            left = dfs(node.left, prev_max)
            right = dfs(node.right, prev_max)

            count += left + right

            return count

        return dfs(root, root.val)


            