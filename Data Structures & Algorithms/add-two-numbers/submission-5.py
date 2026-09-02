# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse linked lists
        curr1 = l1
        curr2 = l2

        prev1 = None
        while curr1:
            next = curr1.next
            prev1, curr1.next = curr1, prev1
            curr1 = next
        
        prev2 = None
        while curr2:
            next = curr2.next
            prev2, curr2.next = curr2, prev2
            curr2 = next
        
        str1 = []
        str2 = []

        curr1 = prev1
        curr2 = prev2

        while curr1:
            str1.append(str(curr1.val))
            curr1 = curr1.next
        
        while curr2:
            str2.append(str(curr2.val))
            curr2 = curr2.next
        
        str1 = "".join(str1)
        str2 = "".join(str2)
        res = str(int(str1) + int(str2))

        dummy = ListNode()
        curr = ListNode()
        dummy.next = curr

        for i in range(len(res)):
            curr.val = int(res[i])

            if i != (len(res) - 1):
                curr.next = ListNode()
            
            curr = curr.next
        
        prev = None
        curr = dummy.next
        while curr:
            next = curr.next
            prev, curr.next = curr, prev
            curr = next
        
        return prev

            