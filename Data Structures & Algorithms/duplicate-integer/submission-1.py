class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for n in nums:
            c=0
            for i in nums:
                if(n==i):
                    c = c+1
            if(c!=1):
                return True
        return False