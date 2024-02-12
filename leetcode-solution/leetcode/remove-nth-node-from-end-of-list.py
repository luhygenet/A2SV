# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        ahead, back = dummy, dummy
        ahead.next, back.next = head, head

        for i in range(n):
            ahead = ahead.next
        while ahead.next:
            ahead = ahead.next
            back = back.next

        back.next = back.next.next
        return dummy.next

        #while curr 












