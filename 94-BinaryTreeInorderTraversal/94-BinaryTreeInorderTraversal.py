// Last updated: 3/3/2025, 7:11:06 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            root = stack.pop()
            result.append(root.val)
            root = root.right
        
        return result



            