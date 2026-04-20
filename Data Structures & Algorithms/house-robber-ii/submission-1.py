class Solution:
    def rob(self, nums: List[int]) -> int:
        memo1 = [None] * (len(nums))
        memo2 = [None] * (len(nums))
        def house(h,memo,nums):
            if h>=len(nums):
                return 0
            if memo[h]:
                return memo[h]
            h1 = nums[h] + house(h+2,memo,nums)
            h2 = house(h+1,memo,nums)
            memo[h] = max(h1,h2)
            return memo[h]
        
        c1=house(0,memo1,nums[1:])
        c2=house(0,memo2,nums[:-1])
        if len(nums) ==1: 
            return nums[0] 
        else:
            return max(c1,c2)