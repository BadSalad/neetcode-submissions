class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def total(i,t):
            if t > amount: return 100000
            if t in memo:
                return memo[t]
            if t == amount:
                return 0
            m = 100000
            for c in coins:
                x = 1 + total(i+1,t+c)
                m = min(m,x)
            memo[t] = m
            return m
        
        out = total(0,0) 
        if out ==100000: 
            return -1 
        else:
            return out