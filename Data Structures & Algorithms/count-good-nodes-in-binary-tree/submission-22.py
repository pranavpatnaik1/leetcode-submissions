# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        maxValue = -101
        def dfs(root, currValue):
            if root is None:
                return

            nonlocal res
            if root.val >= currValue:
                res += 1
                currValue = root.val 
            
            dfs(root.left, currValue)
            dfs(root.right, currValue)
             
        dfs(root, maxValue)
        return res
