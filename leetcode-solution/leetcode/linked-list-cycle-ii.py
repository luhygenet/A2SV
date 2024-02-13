# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: break
        if not fast or not fast.next: return
        slow2 = head
        while fast:
            if slow2 == fast:return fast
            slow2 = slow2.next
            fast = fast.next   
        return 


        
        