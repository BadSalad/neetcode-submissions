class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    visit.add((r,c))
                    q.append((r,c))

        def add(r,c):
            if (r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0 or (r,c) in visit):
                return
            visit.add((r,c))
            q.append((r,c))

        d = 0 if q else 1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = d
                add(r+1,c)
                add(r-1,c)
                add(r,c+1)
                add(r,c-1)
            d+=1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    return -1
        
        return d-1