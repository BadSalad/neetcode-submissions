# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res =[]
        def good(root,lis):
            c = 0
            if not root:
                return 0
            
            if lis and root.val >= max(lis):
                c+=1
            
            lis.append(root.val)
            lis2 = lis[:]
            c += good(root.left,lis)
            c += good(root.right,lis2)

            return c
        c1 = good(root,res)
        return c1+1
            
            
            
        