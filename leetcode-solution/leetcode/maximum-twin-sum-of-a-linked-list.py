# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        while fast:
            fast = fast.next.next
            slow = slow.next
        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        maxi = prev.val + head.val
        while prev and prev.next:
            prev = prev.next
            head = head.next
            maxi = max(prev.val + head.val,maxi)
        return maxi
            
        
            
