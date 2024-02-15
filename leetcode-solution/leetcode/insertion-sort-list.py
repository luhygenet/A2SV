# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        current = head
        while current:
            check = head
            while current != check:
                if check.val > current.val:
                    check.val, current.val = current.val, check.val
                check = check.next
            current = current.next
        return head
