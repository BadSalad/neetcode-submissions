class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board),len(board[0])
        directions =[[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        visit = set()

        def bfs(r,c):
            q.append((r,c))
            visit.add((r,c))
            while q:
                row,col = q.popleft()
                for x,y in directions:
                    ro,co = row+x,col+y
                    if (ro in range(rows)) and (co in range(cols)) and ((ro,co) not in visit) and ((board[ro][co]=="O")):
                        q.append((ro,co))
                        visit.add((ro,co))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    if r==0 or c==0 or r==rows-1 or c==cols-1:
                        bfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and (r,c) not in visit:
                    board[r][c] = "X"