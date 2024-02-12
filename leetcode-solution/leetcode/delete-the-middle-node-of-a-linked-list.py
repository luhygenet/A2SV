# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        dummy  = ListNode()
        dummy.next = head
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            dummy = dummy.next
            slow = slow.next
        print(dummy.next.val)
        dummy.next = dummy.next.next
        return head
