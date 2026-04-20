class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visit =set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        rows,cols = len(matrix), len(matrix[0])
        res = []
        def spiral(r,c,d,count):
            if count == (rows*cols): return
            x,y = directions[d]
            if r not in range(0,rows) or c not in range(0,cols) or (r,c) in visit:
                r= r-x
                c= c-y
                if d == 3:
                    d = 0
                else:
                    d+=1
                x1,y1 = directions[d]
                spiral(r+x1,c+y1,d,count)
            else:
                res.append(matrix[r][c])
                visit.add((r,c))
                spiral(r+x,c+y,d,count+1)
        spiral(0,0,0,0)
        return res