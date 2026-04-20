class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        out =0
        while i < len(prices)-1:
            j = i+1
            max_profit = max(prices[j:]) - prices[i]
            out = max(out,max_profit)
            i += 1

        return out
        