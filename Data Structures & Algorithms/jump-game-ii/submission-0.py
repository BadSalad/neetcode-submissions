class Solution:
    def jump(self, nums: List[int]) -> int:
        def jump(i):
            if i==len(nums)-1:
                return 0
            if i>len(nums)-1 or nums[i]==0:
                return 1000000
            out = 100000
            for j in range(1,nums[i]+1):
                steps = 1 + jump(i+j)
                out = min(out,steps)
            return out
        return jump(0)