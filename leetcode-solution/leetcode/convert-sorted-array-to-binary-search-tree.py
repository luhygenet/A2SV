# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def make(l,r):
            if l > r:
                return None
            mini = (l + r)//2
            root = TreeNode(nums[mini])
            root.left = make(l,mini-1)
            root.right = make(mini+1,r)  
            return root
        return make(0,len(nums)-1)
        
        
