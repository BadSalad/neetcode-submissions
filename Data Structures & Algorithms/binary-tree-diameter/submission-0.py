# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def max_depth(node):
            if not node:
                return 0
            
            l = max_depth(node.left)
            r = max_depth(node.right)

            return 1 + max(l,r)

        left = max_depth(root.left)
        right = max_depth(root.right)

        diameter = left+right

        l1 = self.diameterOfBinaryTree(root.left)
        r1 = self.diameterOfBinaryTree(root.right)

        return max(diameter,l1,r1)