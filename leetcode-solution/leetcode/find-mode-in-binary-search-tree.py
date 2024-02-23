# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hashi = defaultdict(int)
        lis = []
        def find(root):
            nonlocal hashi
            if not root:
                return None
            if root not in lis:
                hashi[root.val] += 1
                lis.append(root)
            find(root.left)
            find(root.right)
        find(root) 
        val = max(hashi.values())
        maxi = []
        for i in hashi:
            if hashi[i] == val:
                maxi.append(i) 
        return maxi     
        
