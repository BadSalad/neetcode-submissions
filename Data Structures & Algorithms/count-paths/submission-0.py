class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [[1,0],[0,1]]
        visit = set()
        def path(x,y):
            if x >=m or y>=n or x<0 or y<0 or (x,y) in visit:
                return 0
            if x==m-1 and y==n-1: return 1
            visit.add((x,y))
            out = 0
            for r,c in directions:
                out +=path(x+r,y+c)
            visit.remove((x,y))
            return out
        
        return path(0,0)