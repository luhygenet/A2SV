# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        trav = head
        trav2 = head.next
        while trav2:
            if trav.val == trav2.val:
                trav.next = trav2.next
                trav2 = trav2.next
            else:
                trav = trav.next
                trav2 = trav2.next
        return head
        
        
            