class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def total(i, t):
            if t > amount:
                return 0
            if t == amount:
                return 1
            if (i, t) in memo:
                return memo[(i, t)]

            m = 0
            for j in range(i, len(coins)):   # ✅ use index control
                m += total(j, t + coins[j])

            memo[(i, t)] = m
            return m

        return total(0, 0)
