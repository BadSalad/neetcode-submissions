class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def tar(i,t):
            if i>=len(nums):
                if t==target: return 1
                return 0
            return tar(i+1, t-nums[i]) + tar(i+1,t+nums[i])
        return tar(0,0)