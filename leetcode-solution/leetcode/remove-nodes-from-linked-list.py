# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        trav = prev
        trav2 = prev.next
        while trav2:
            if trav.val > trav2.val:
                trav.next = trav2.next
                trav2 = trav2.next
            else:
                trav = trav.next
                trav2 = trav2.next
        new_rev = None
        curr = prev
        while curr:
            temp = curr.next
            curr.next = new_rev
            new_rev = curr
            curr = temp
        return new_rev
        
        
            
            

