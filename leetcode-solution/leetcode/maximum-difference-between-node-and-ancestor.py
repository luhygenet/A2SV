# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        small = root.val
        large = root.val
        final = 0
        def ds(root,left,right):
            nonlocal final
            if not root:
                final = max(final,abs(right - left))
                return
            ds(root.left,min(root.val,left),max(root.val,right))
            ds(root.right,min(root.val,left),max(root.val,right))
        ds(root,small,large)
        return final
            