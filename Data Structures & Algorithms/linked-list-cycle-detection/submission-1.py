# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycleSet = set()
        cycleCheck = True
        curr = head

        while curr and cycleCheck:
            if curr in cycleSet:
                cycleCheck = False
            else:
                cycleSet.add(curr)
            
            curr = curr.next
        
        if not cycleCheck:
            return True
        else:
            return False