class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2 = 1,1
        t = 0
        if n == 1: return 1
        i=1
        while i<n:
            t=n2
            n2 = n1+n2
            n1=t
            i+=1
        return n2