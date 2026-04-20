class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hmap = {i:[] for i in range(numCourses)}
        visit = set()
        out =[]
        for c,p in prerequisites:
            hmap[c].append(p)
        
        def dfs(c):
            if c in visit:
                return False
            if hmap[c] == []:
                if c not in out:
                    out.append(c)
                return True
            visit.add(c)
            for x in hmap[c]:
                if not dfs(x):
                    return False
            visit.remove(c)
            hmap[c] == []
            if c not in out:
                out.append(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return out