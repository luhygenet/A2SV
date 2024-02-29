# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level = [root]
        ans = [[root.val]]
        flag = False

        while level:
            next_level = []
            current = []
            
            for node in level:
                if node.left:
                    next_level.append(node.left)
                    current.append(node.left.val)

                if node.right:
                    next_level.append(node.right)
                    current.append(node.right.val)
            if current:
                if flag:
                    ans.append(current)

                else:
                    ans.append(current[::-1])

            flag = not flag
            level = next_level

        return ans       
            
            