# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:        

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.nodes = set()
        root.val = 0
        def dfs(node):
            if node is None:
                return TreeNode(0)

            self.nodes.add(node.val)
            if node.left:
                left_val = node.val * 2 + 1
                node.left.val = left_val
                left_tree = dfs(node.left)
            
            if node.right:
                right_val = node.val * 2 + 2
                node.right.val = right_val
                right_tree = dfs(node.right)
            
            return root

        dfs(root)
        
    def find(self, target: int) -> bool:
        return target in self.nodes

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)