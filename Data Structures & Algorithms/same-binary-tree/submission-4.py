# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(rootP, rootQ):
            if not rootP and not rootQ:
                return True
            elif not rootP or not rootQ:
                return False

            left = dfs(rootP.left, rootQ.left)
            right = dfs(rootP.right, rootQ.right)

            check = (rootP.val == rootQ.val) and left and right
            
            return check
        
        return dfs(p, q)
