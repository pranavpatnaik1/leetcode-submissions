# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = 0
        def dfs(root, lowerBound, upperBound) -> None:
            if root is None:
                return 
            
            if root.val > lowerBound and root.val < upperBound:
                dfs(root.left, lowerBound, root.val)
                dfs(root.right, root.val, upperBound)
            else:
                nonlocal res
                res += 1
        
        dfs(root, -1000000001, 1000000001)

        return False if res > 0 else True
