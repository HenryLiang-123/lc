# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        result = []
        i = 0
        def dfs(left, right):
            res = []
            if left > right:
                res.append(None)
                return res

            for i in range(left, right + 1):
                
                left_tree = dfs(left, i-1)
                right_tree = dfs(i+1, right)
                for l in left_tree:
                    for r in right_tree:
                        root = TreeNode(i+1)
                        root.left = l
                        root.right = r
                        res.append(root)

            return res

        return (dfs(0, n-1))
        # return result