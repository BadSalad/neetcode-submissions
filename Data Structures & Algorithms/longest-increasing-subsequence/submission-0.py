class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def lis(c,p):
            if c==len(nums): return 0
            if nums[c] > nums[p]:
                return max(1+lis(c+1,c),lis(c+1,p))
            return lis(c+1,p)
        out = 0
        for i in range(len(nums)-1):
            out = max(out,lis(i+1,i))
        return out+1