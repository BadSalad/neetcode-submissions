# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(node):
            lis = []
            if node.left:
                lis += inOrder(node.left)
            
            lis.append(node.val)

            if node.right:
                lis += inOrder(node.right)
            
            return lis
        
        res = inOrder(root)

        return res[k-1]