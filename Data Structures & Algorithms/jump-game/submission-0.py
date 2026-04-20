class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def jump(i):
            if i==len(nums)-1:
                return True
            if i>len(nums)-1 or nums[i]==0:
                return False
            res = False
            for j in range(1,nums[i]+1):
                res = res or jump(i+j)
            return res
        return jump(0)