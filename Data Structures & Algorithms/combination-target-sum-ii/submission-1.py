class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]
        subset = []

        def dfs(i,total):
            if total == target:
                 res.append(subset[:])
                 return
            if i>=len(nums) or total > target:
                return

            subset.append(nums[i])
            dfs(i+1,total+nums[i])

            subset.pop()
            dfs(i+1,total)

        dfs(0,0)    
        out = []
        unique = set()
        for sublist in res:
            if tuple(sorted(sublist)) not in unique:
                out.append(sublist)
                unique.add(tuple(sorted(sublist)))

        return out