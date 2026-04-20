class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxR(num):
            t,n1,n2=0,0,0
            for n in num:
                t = n2
                n2 = max(n+n1,n2)
                n1 = t
            return n2
        
        return max(nums[0],maxR(nums[1:]),maxR(nums[:-1]))