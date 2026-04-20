class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<r:
            m = (l+r)//2
            if(nums[m]>=nums[r]):
                l = m+1
            else:
                r = m
        pivot = l

        def BinarySearch(left,right,lis,target):
            while(left<=right):
                mid = (right+left)//2
                if(lis[mid]>target):
                    right = mid -1
                elif(lis[mid]<target):
                    left = mid + 1
                else:
                    return mid
            return -1

        res = BinarySearch(0,pivot-1,nums,target)

        if(res!=-1):
            return res
        else:
            return BinarySearch(pivot,len(nums)-1,nums,target)

            
