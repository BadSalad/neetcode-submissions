class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [0]*len(nums)
        for i in range(len(nums)):
            pro = 1
            for j in range(len(nums)):
                if(i!=j):
                    pro *= nums[j]
                out[i] = pro


        return out
