# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque()
        level = 0
        tmp = []

        queue.append(root)

        while queue:
            lenQ = len(queue)

            for i in range(lenQ):
                currNode = queue.popleft()
                if i == 0:
                    tmp.append(currNode.val)

                if currNode.right:
                    queue.append(currNode.right)
                if currNode.left:
                    queue.append(currNode.left)
                
            
            level += 1
        
        return tmp



