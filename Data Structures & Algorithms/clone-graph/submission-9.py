"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldNewMap = dict()
        def checkGraph(checkNode):
            if checkNode in oldNewMap:
                return oldNewMap[checkNode]
            
            newNode = Node(checkNode.val, [])
            oldNewMap[checkNode] = newNode
            
            for neighbor in checkNode.neighbors:
                if neighbor:
                    newNode.neighbors.append(checkGraph(neighbor))
            
            return newNode
        
        return checkGraph(node)