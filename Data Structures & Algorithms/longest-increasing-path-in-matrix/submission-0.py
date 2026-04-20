class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        directions = ([1,0],[0,1],[-1,0],[0,-1])
        rows, cols = len(matrix), len(matrix[0])
        def lip(i,j):
            m = 0
            for (x,y) in directions:
                r,c = i+x,j+y
                if r < 0 or c < 0 or r >= rows or c >= cols:
                    continue
                if matrix[r][c] > matrix[i][j]:
                    if (i,j) in memo:
                        m=max(m,memo[(i,j)])
                    else:
                        m=max(m,1+lip(r,c))
            memo[(i,j)] = m
            return memo[(i,j)]

        out = 0
        for k in range(rows):
            for l in range(cols):
                out = max(out, lip(k,l))
        
        return 1+out
                                          