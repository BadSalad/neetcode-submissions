class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)
        def steps(s):
            if s == n: return 1
            if s>n: return 0
            if memo[s] != -1: return memo[s]
            memo[s] = steps(s+1) + steps(s+2)
            return memo[s]
        
        return steps(0)