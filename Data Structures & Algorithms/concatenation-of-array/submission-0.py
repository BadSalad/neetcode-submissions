class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = []
        for i in range(2*n):
            if i<n:
                out.append(nums[i])
            else:
                out.append(nums[i-n])
        return out