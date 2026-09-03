# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # def height(root):
        #     if root is None:
        #         return -1
            
        #     leftHeight = height(root.left)
        #     rightHeight = height(root.right)

        #     return max(leftHeight, rightHeight) + 1

        # def dfs(root):
        #     if root is None:
        #         return True
            
        #     leftHeight = height(root.left)
        #     rightHeight = height(root.right)

        #     if abs(leftHeight - rightHeight) > 1:
        #         return False
        #     else:
        #         return True
        
        # return dfs(root.right) and dfs(root.left)

        def dfs(root):
            if not root:
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            balanced = (abs(left[1] - right[1]) <= 1) and left[0] and right[0]
            
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]


