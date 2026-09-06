# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder = []
        # def dfs(root) -> None:
        #     if root is None:
        #         return
            
        #     dfs(root.left)
        #     inorder.append(root.val)
        #     dfs(root.right)
        
        # dfs(root)
        # return inorder[k-1]

        count = k
        res = 0
        def dfs(root) -> None:
            if root is None:
                return 0
            
            nonlocal count, res
            dfs(root.left)
            count -= 1

            if count == 0:
                res += root.val

            dfs(root.right)
        
        dfs(root)
        return res