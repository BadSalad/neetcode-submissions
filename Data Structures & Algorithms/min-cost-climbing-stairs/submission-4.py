class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n1,n2,t = 0,0,0
        n = len(cost)-1
        while n>=0:
            minC = min(cost[n]+n1,cost[n]+n2)
            t= n1
            n1 = minC
            n2 = t
            n-=1
        return min(n1,n2)
             

        