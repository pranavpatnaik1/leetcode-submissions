# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # res = []
        # def dfs(root, depth):
        #     if not root:
        #         return
            
        #     if depth < len(res):
        #         res[depth].append(root.val)
        #     else:
        #         res.append([root.val])

        #     dfs(root.left, depth + 1)
        #     dfs(root.right, depth + 1)
        
        # dfs(root, 0)
        # return res

        if not root:
            return []

        queue = deque()
        res = []

        queue.append(root)
        
        while queue:
            lenQ = len(queue)
            level = []

            for _ in range(lenQ):
                currNode = queue.popleft()

                level.append(currNode.val)

                if currNode.left:
                    queue.append(currNode.left)
                
                if currNode.right:
                    queue.append(currNode.right)
            
            res.append(level)
        
        return res


