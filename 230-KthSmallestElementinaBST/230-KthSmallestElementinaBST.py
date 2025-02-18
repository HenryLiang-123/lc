// Last updated: 2/18/2025, 1:29:27 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            k -= 1
            curr = stack.pop()
            root = curr.right
            if k == 0:
                return curr.val

            