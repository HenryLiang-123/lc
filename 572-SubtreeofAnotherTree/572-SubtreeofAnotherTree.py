# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root1, root2):
        if root1 is None and root2 is None:
                return True

        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False
        
        return self.check(root1.left, root2.left) and self.check(root1.right, root2.right)
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subroot):
            # print(root.val, subroot.val)
            if root is None:
                return False

            if not self.check(root, subroot):
                return dfs(root.left, subroot) or dfs(root.right, subroot)
            
            return True
                


        return dfs(root, subRoot)