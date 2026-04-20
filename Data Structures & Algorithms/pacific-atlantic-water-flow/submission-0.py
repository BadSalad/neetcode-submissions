class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
            rows, cols = len(heights),len(heights[0])
            pac, atl = set(), set()
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            pq,aq = deque(),deque() 
            
            def bfs(q,visit):
                # q.append((r,c))
                # visit.add((r,c))
                while q:
                    row, col = q.popleft()
                    for x,y in directions:
                        ro,co = row+x, col+y
                        if (ro in range(rows)) and (co in range(cols)) and ((ro,co) not in visit) and (heights[ro][co] >= heights[row][col]):
                            q.append((ro,co))
                            visit.add((ro,co))

            for r in range(rows):
                for c in range(cols):
                    if r==0 or c==0:
                        pq.append((r,c))
                        pac.add((r,c))
                    if r==rows-1 or c == cols-1:
                        aq.append((r,c))
                        atl.add((r,c))
            bfs(pq,pac)
            bfs(aq,atl)

            out =[]

            for i in pac:
                for j in atl:
                    if i == j:
                        out.append(i)

            return out