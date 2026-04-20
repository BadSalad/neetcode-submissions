class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Logic is if num-1 doesn't exist then its probably start of a set

        numSet = set(nums)
        out,c = 0,0
        for n in nums:
            if n-1 not in numSet:
                c+=1
                while n+c in numSet:
                    c+=1
            out = max(out,c)
            c=0
        return out