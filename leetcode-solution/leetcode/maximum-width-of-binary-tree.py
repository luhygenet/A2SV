# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root,1))
        maxi = 0 
        

        while q:
            length = len(q)
            print(q[-1][-1])

            maxi = max(maxi, q[-1][-1] - q[0][1] +1 )

            for i in range(length):
                curr = q[0][0]
                j = q[0][1]

                if curr.left:
                    q.append((curr.left, 2*j))
                if curr.right:
                    q.append((curr.right, 2*j + 1))
                q.popleft()
        return maxi
