class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while(l<=r):
            mid = (l+r)//2
            if((nums[mid]-nums[l])>(nums[mid]-nums[r])):
                r = mid-1
            else:
                l=l+1
        return nums[mid]
        