class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [None] * (len(nums))
        def house(h,memo):
            if h>=len(nums):
                return 0
            if memo[h]:
                return memo[h]
            h1 = nums[h] + house(h+2,memo)
            h2 = house(h+1,memo)
            memo[h] = max(h1,h2)
            return memo[h]
        
        return house(0,memo)