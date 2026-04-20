class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        m = nums[-1]
        for i in range(len(nums)-3,-1,-1):
            m = max(m,nums[i+2])
            nums[i] = max(nums[i] + nums[i+2], nums[i+1], nums[i]+m)
        return max(nums[0], nums[1])