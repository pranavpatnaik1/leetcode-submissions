# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Edge cases:
        # Empty LL [X]
        # First node [X]

        if head.next is None:
            return None

        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        # print(length)
        if n == length:
            return head.next

        tmp = length - n - 1 # n = corrective step

        prevNode = head
        for i in range(tmp):
            prevNode = prevNode.next

        # reached node to remove
        prevNode.next = prevNode.next.next

        return head





