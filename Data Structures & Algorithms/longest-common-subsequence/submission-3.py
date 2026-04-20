class Solution:
    def longestCommonSubsequence(self, text: str, text2: str) -> int:
        rows, cols = len(text), len(text2)
        mat = [[None for _ in range(cols)] for _ in range(rows)]

        def lcs(i,j):
            if i>=rows or j>=cols: return 0
            if mat[i][j]:
                return mat[i][j]
            if text[i] == text2[j]:
                mat[i][j] = max(1+lcs(i+1,j+1),lcs(i+1,j),lcs(i,j+1))
            else:
                mat[i][j] = max(lcs(i+1,j),lcs(i,j+1))
            return mat[i][j]

        return lcs(0,0)
