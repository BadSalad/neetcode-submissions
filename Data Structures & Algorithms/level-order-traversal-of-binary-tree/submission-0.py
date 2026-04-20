# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashSet = defaultdict(lambda: [])
        
        def levels(root,level,lis):
            if not root:
                return None
            lis[level].append(root.val)

            levels(root.left,level+1,lis)
            levels(root.right,level+1,lis)
            
            return None

        levels(root,0,hashSet)

        return list(hashSet.values())


        
        