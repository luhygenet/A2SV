# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        if slow == None:
            return head
        fast = head.next
        fast2 = fast
        while slow.next and slow.next.next:
            slow.next = slow.next.next
            fast.next = fast.next.next
            slow = slow.next
            fast = fast.next       
        slow.next = fast2
        return head
        


        
    