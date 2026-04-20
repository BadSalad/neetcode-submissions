class Solution:
    def validTree(self, num: int, edges: List[List[int]]) -> bool:
        hmap = {i:[] for i in range(num)}
        visit, out = set(),set()
        
        for n,e in edges:
            if n == e:
                return False
            hmap[n].append(e)
            hmap[e].append(n)
        
        def dfs(n,p):
            if n in visit:
                return False
            if n in out:
                return True
            visit.add(n)
            for x in hmap[n]:
                if x!= p and not dfs(x,n): return False
            visit.remove(n)
            out.add(n)
            return True
        
        if not dfs(0,0): return False
        
        if len(out)==num:
            return True
        return False
