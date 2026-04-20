# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(node,c):
            if c== k:
                return []

            lis = []
            if node.left:
                lis += inOrder(node.left,c)
            
            lis.append(node.val)
            c += 1

            if node.right:
                lis += inOrder(node.right,c)
            
            return lis
        
        res = inOrder(root,0)

        return res[k-1]