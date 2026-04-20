class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        g = 0

        def compute(i):
            g = gas[i] - cost[i]
            if i==(len(gas)-1):
                j = 0 
            else:
                j = i+1 
            while g >= 0 and j != i:
                g = g + gas[j] - cost[j]
                if j==(len(gas)-1):
                    j = 0 
                else:
                    j = j+1
            if j!=i or g<0: return False
            return True

        for x in range(len(gas)):
            if compute(x): return x
        return -1 