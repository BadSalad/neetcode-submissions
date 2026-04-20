class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visit = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            area = 1
            while q:
                row,col = q.popleft()
                for x,y in directions:
                    ro = row + x
                    co = col + y
                    if((ro in range(rows)) and (co in range(cols) and (grid[ro][co]== 1) and ((ro,co) not in visit))):
                        area += 1
                        q.append((ro,co))
                        visit.add((ro,co))
            return area
        out = 0
        a = 0
        for r in range(rows):
            for c in range(cols):
                if((grid[r][c] == 1) and ((r,c) not in visit)):
                    a = bfs(r,c)
                    out = max(out,a)

        return out