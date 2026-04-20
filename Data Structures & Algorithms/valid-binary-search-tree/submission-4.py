# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inOrder(node):
            lis = []
            if node.left:
                lis += inOrder(node.left)
            
            lis.append(node.val)

            if node.right:
                lis += inOrder(node.right)
            
            return lis
        
        res = inOrder(root)

        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False
        return True