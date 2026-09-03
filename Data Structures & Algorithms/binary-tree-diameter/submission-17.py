# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Find height of left and right subtree
        maxDiameter = 0
        def findHeight(root: Optional[TreeNode]):
            nonlocal maxDiameter

            if root is None:
                return -1

            leftHeight = findHeight(root.left)
            rightHeight = findHeight(root.right)

            diameter = leftHeight + rightHeight + 2
            maxDiameter = max(maxDiameter, diameter)

            return max(leftHeight, rightHeight) + 1
        
        findHeight(root)
        return maxDiameter
            

