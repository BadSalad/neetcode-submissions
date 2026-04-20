class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:   #SKIPS DUPLICATES
                continue
            j = i + 1
            k = len(nums) - 1
            while (j<k):
                if(j>i+1 and nums[j] == nums[j - 1]):
                    j = j +1
                    continue
                if(k<len(nums) - 1 and nums[k] == nums[k + 1]):
                    k = k - 1
                    continue
                val = nums [i] + nums [j] + nums[k]
                if(val==0):
                    temp = [nums[i],nums[j],nums[k]]
                    out.append(temp)
                    j = j + 1 
                    k = k - 1
                elif (val < 0):
                    j = j + 1
                else:
                    k = k -1
        return out
        