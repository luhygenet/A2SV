# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        dummy = head
        length = 0
        while dummy:
            dummy = dummy.next
            length += 1
        quotient = length//k
        extras = length % k
        arr = []
        dummy = head
        for i in range(k):
            arr.append(dummy)
            print(arr)
            for i in range(quotient-1):
                    if not dummy:break
                    dummy = dummy.next
            if extras and quotient-1>=0:
                    if not dummy: continue
                    dummy = dummy.next
                    extras -= 1
            if dummy:
                dummy.next,dummy = None,dummy.next
        return arr

        