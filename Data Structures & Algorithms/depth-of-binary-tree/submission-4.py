# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        if root is None:
            return 0
            
        def checkDepth(root, depth):
            if root is None:
                nonlocal maxDepth
                maxDepth = max(depth - 1, maxDepth)
                return
            
            checkDepth(root.left, depth + 1)
            checkDepth(root.right, depth + 1)
        
        checkDepth(root, 0)
        return maxDepth + 1