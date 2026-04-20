class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [None]*(n+1)
        
        def stairs(n,memo):
            if memo[n]:
                return memo[n]
            elif n==1:
                result = 1
            elif n==2:
                result = 2
            else:
                result = stairs(n-1,memo) + stairs(n-2,memo)
            memo[n]=result
            return result
        
        return stairs(n,memo)