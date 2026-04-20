class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [None] * (len(cost)+1)
        def stairs(s,memo):
            if s>=len(cost):
                return 0
            if memo[s]:
                return memo[s]
            result = cost[s] + min(stairs(s+1,memo),stairs(s+2,memo))
            memo[s] = result
            return result
        return min(stairs(0,memo),stairs(1,memo))