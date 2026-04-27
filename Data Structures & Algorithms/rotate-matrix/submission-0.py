class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        temp = [row[:] for row in matrix]
        for r in range(n):
            row = matrix[r]
            for c in range(n):
                temp[c][n-r-1] = row[c]
        
        for r in range(n):
            for c in range(n):
                matrix[r][c] = temp [r][c]
                 