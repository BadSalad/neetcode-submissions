class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        island = 0
        row, cols = len(grid), len(grid[0])
        visited = set()
        
        def bfs(r,c):
            q= collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                ro,co = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for x,y in directions:
                    r = ro + x
                    c = co + y
                    if((r in range(row)) and (c in range(cols)) and (grid[r][c]=="1") and ((r,c) not in visited)):
                        visited.add((r,c))
                        q.append((r,c))

        
        
        for r in range(row):
            for c in range(cols):
                if ((grid[r][c] == "1") and ((r,c) not in visited)):
                    bfs(r,c)
                    island += 1
        
        return island