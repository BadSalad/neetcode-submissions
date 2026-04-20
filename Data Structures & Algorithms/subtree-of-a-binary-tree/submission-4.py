# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False

        comp,left,right = False , False , False

        if self.compare(root,subRoot):
            return True
        
        else:
            left = self.isSubtree(root.left,subRoot)
            right = self.isSubtree(root.right,subRoot)
        
        return comp or left or right
    
    def compare(self, p, q):
        if not p and not q:
                return True
        
        if p and q:      
            left = self.compare(p.left,q.left)
            right = self.compare(p.right,q.right)

            return (p.val==q.val) and left and right
        
        else:
            return False