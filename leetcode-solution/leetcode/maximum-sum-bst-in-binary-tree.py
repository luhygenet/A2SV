# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        def trav(root):
            nonlocal max_sum
            if not root:
                return 0, float("-inf"), float("inf")
            left_sum, left_min, left_max = trav(root.left)
            right_sum, right_min, right_max = trav(root.right)  

            if (not root.left or (root.left and root.val > left_max)) and \
           (not root.right or (root.right and root.val < right_min)):

                curr_sum = left_sum + right_sum + root.val
                max_sum = max(curr_sum, max_sum)
                return curr_sum, left_min if root.left else root.val, right_max if root.right else root.val

            else:
                return float("-inf"), float("-inf"),float("inf")

        trav(root)
        return max_sum