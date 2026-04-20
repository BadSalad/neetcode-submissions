# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = defaultdict(lambda: [])

        def view(root, level, lis):
            if not root:
                return None

            lis[level].append(root.val)

            view(root.left,level+1,lis)
            view(root.right,level+1,lis)
        
        view(root,0,res)
        res = list(res.values())
        out = []
        for i in res:
            out.append(i[-1])

        return out
            
        