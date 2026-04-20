# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p:
            if not q:
                return True
            else:
                return False

        if not q:
            if not p:
                return True
            else:
                return False
                
        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right,q.right)

        return (p.val==q.val) and left and right