# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greater = ListNode()
        smaller = ListNode()
        curr = head
        first_half = smaller
        second_half = greater
        while curr:
            if curr.val < x:
                smaller.next = curr
                smaller = smaller.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next
        if smaller.next and smaller.next.val > smaller.val:
            smaller.next = None
        if greater.next and greater.next.val < greater.val:
            greater.next = None
        smaller.next = second_half.next
        return first_half.next
        
        
        







                