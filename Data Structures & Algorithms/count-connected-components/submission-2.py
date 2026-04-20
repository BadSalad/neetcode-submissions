class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hmap = {i:[] for i in range(n)}
        visit = set()

        for a,b in edges:
            hmap[a].append(b)
            hmap[b].append(a)
        
        def dfs(node,p):
            if node in visit:
                return 0
            visit.add(node)
            for nei in hmap[node]:
                if nei!=p: dfs(nei,node)
            return 1
        c = 0
        for i in range(n):
            c = c + dfs(i,-1)
            # if len(visit) != n and i not in visit:
            #     c+=1

        return c