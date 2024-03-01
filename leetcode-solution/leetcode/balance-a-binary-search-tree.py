# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        li = []
        def rec(root):
            if not root:
               return None
            li.append(root.val)
            rec(root.left)
            rec(root.right)
            
        rec(root)
        li.sort()
        # new_root = li[len(li)-1//2]
        print(((len(li)-1)//2))
        def make(l,r):
            if l > r:
                return None
            mini = (l + r)//2
            root = TreeNode(li[mini])
            root.left = make(l,mini-1)
            root.right = make(mini+1,r)  
            return root
        return make(0,len(li)-1)
        

            

       
