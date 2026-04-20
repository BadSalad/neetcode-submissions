class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i,total):
            if total == target:
                res.append(subset.copy())
                return
            if i>=len(nums) or total > target:
                return
            
            subset.append(nums[i])
            dfs(i,total + nums[i])   ##this total + nums ensures in the wrapper fuinction the value of total is always ine element less to avoid an infinite loop

            subset.pop()
            dfs(i+1,total)

        dfs(0,0)
        return res
        