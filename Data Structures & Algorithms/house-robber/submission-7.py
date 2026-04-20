class Solution:
    def rob(self, nums: List[int]) -> int:
        maxC,n1,n2 = 0,0,0
        for n in nums:
            t= n2
            n2 = max(n+n1,n2)
            n1=t
        return n2