# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(root):
            if not root:
                return

            left = dfs(root.left)
            # if left:
            #     result.append(left.val)
            result.append(root.val)
            right = dfs(root.right)
            # if right:
            #     result.append(right.val)
            
            return root

        dfs(root)
        return result


            