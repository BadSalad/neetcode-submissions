class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        rows = len(prerequisites)
        hmap = defaultdict(list)
        visit = set()

        for i in prerequisites:
            hmap[i[0]].append(i[1])

        def pre(x, visit, i):
            bool = True
            for c in x:
                if c in hmap and c not in visit:
                    visit.add(c)
                    bool = bool and pre(hmap[c], visit, i)
                    visit = set()
                    visit.add(i)
                elif c in visit:
                    return False
                else:
                    # visit = set()
                    # visit.add(i)
                    continue
            return bool

        for i in range(numCourses):
            visit = set()
            if i in hmap:
                visit.add(i)
                if not pre(hmap[i], visit, i):
                    return False
        
        return True

        