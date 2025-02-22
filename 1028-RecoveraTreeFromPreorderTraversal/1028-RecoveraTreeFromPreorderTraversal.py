// Last updated: 2/22/2025, 3:28:01 PM
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i = 0
        n = len(traversal)

        def dfs(depth):
            nonlocal i
            if i >= n:
                return None

            # Count dashes to determine the depth
            start = i
            while i < n and traversal[i] == "-":
                i += 1
            dashcount = i - start

            # If the depth doesn't match, backtrack
            if dashcount != depth:
                i -= dashcount  # Reset index
                return None

            # Read the number (multi-digit support)
            start = i
            while i < n and traversal[i].isdigit():
                i += 1
            value = int(traversal[start:i])

            # Create the current node
            root = TreeNode(value)
            root.left = dfs(depth + 1)
            root.right = dfs(depth + 1)

            return root

        return dfs(0)
