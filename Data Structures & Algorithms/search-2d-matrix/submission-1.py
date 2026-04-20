class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col =  len(matrix),len(matrix[0])
        for m in matrix:
            if m[col-1] >= target:
                l,r = 0,col-1
                while l<=r:
                    mid = (l+r)//2
                    if target == m[mid]: return True
                    elif target <m[mid]: r=mid-1
                    else: l=mid+1
                return False
        return False