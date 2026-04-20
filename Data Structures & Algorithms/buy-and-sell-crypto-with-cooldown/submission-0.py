class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def stock(i,p):
            if i>=len(prices): 
                return 0
            if (i, p) in memo:
                return memo[(i, p)]     
            if p == -1:
                memo[(i, p)] = max(stock(i+1,prices[i]),stock(i+1,p))
            elif prices[i]>p:
                memo[(i, p)] = max(((prices[i]-p) + stock(i+2,-1)),stock(i+1,p))
            else:
                memo[(i, p)] = stock(i+1,p)
            return memo[(i, p)]
        
        return stock(0,-1)