# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        traverseP = []
        traverseQ = []

        def traverse(root,target,lis):
            lis.append(root)
            if root.val > target.val:
                traverse(root.left,target,lis)
            elif root.val < target.val:
                traverse(root.right,target,lis)
            else:
                return None

        traverse(root,p,traverseP)
        traverse(root,q,traverseQ)

        res = 0
        length = min(len(traverseP),len(traverseQ))
        for i in range(length):
            if traverseP[i].val==traverseQ[i].val:
                res = traverseP[i]
        
        return res

        
        