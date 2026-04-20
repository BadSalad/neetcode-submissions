class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        maxP = 0
        minP = 0
        out = 0
        for i in range(len(nums)):
            if i == 0:
                maxP = nums[i]
                minP = nums[i]
                out = nums[i]
                continue
            maxP = max(nums[i],nums[i]+maxP)
            # minP1 = min(nums[i],nums[i]+maxP,nums[i]*minP)
            # maxP, minP = maxP1, minP1
            out = max(out,maxP)
        return out