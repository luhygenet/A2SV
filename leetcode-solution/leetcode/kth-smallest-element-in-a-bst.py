# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def iterate(root):
            nonlocal res
            if not root:
                return 
            res.append(root.val)
            iterate(root.left)
            iterate(root.right)
        iterate(root)
        res.sort()
        return res[k-1]
