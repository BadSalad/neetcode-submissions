class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hmap = {i:[] for i in range(numCourses)}
        visit = set()

        for crs, pre in prerequisites:
            hmap[crs].append(pre)

        def dfs(c):
            if c in visit:
                return False
            if hmap[c] == []:
                return True
            visit.add(c)
            for x in hmap[c]:
                if not dfs(x): 
                    return False
            visit.remove(c)
            hmap[c] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
