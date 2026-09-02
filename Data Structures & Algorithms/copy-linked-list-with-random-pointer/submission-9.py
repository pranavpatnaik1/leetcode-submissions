"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyDict = dict()

        curr = head
        while curr:
            newNode = Node(curr.val)
            copyDict[curr] = newNode 

            curr = curr.next

        copyDict[curr] = None

        curr = head
        dummy = Node(4)
        dummy.next = copyDict[curr]

        while curr:
            # Given original node, translate
            copyDict[curr].next = copyDict[curr.next]
            copyDict[curr].random = copyDict[curr.random]

            curr = curr.next

        # dummy.next = copyDict[dummy.next.next]
        # dummy.next.next = copyDict[dummy.next.next.next]

        
        return dummy.next

