class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum1 = 0
        for n in nums:
            sum1+=n
        if sum1%2!=0:
            return False
        target = sum1/2
        def sums(i,tot):
            if tot == target: return True
            if tot > target or i>len(nums): return False
            if i<len(nums):
                return sums(i+1,tot) or sums(i+1,tot+nums[i])
                
        return sums(0,0)

