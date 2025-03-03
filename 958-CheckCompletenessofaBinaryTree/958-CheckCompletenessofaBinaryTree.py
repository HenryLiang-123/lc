# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            currNode, pos = nodes[i]
            i += 1
            if currNode:
                nodes.append((currNode.left, 2 * pos))
                nodes.append((currNode.right, 2 * pos + 1))
            
        return nodes[-1][1] == len(nodes)