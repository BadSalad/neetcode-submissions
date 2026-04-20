# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def max_depth(node):
            if not node:
                return 0
            
            l = max_depth(node.left)
            r = max_depth(node.right)

            return 1 + max(l,r)

        left = max_depth(root.left)
        right = max_depth(root.right)

        res = (abs(left-right) <= 1)

        l1 = self.isBalanced(root.left)
        r1 = self.isBalanced(root.right)

        return (res and l1 and r1)