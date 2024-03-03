# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(nums):
            if len(nums) == 0:
                return 
            maxi = max(nums)
            maxi_ind = nums.index(maxi)
            created = TreeNode(maxi)
            created.left = rec(nums[:maxi_ind])
            created.right = rec(nums[maxi_ind + 1:])
            return created
        return (rec(nums))
        