// Last updated: 3/4/2025, 1:32:30 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def dfs(left, right):
            if left > right:
                return [None]

            res = []
            for i in range(left, right + 1):
                left_trees = dfs(left, i-1)
                right_trees = dfs(i+1, right)
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i+1)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res

        return dfs(0, n-1)