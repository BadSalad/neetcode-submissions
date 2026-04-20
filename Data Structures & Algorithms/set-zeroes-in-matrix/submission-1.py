class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows,cols = len(matrix),len(matrix[0])
        vr,vc = set(),set()
        def zero():
            for r in vr: matrix[r] = [0]*(cols)
            for c in vc:
                for i in range(rows): matrix[i][c] = 0
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]==0:
                    vr.add(row)
                    vc.add(col)
        zero()