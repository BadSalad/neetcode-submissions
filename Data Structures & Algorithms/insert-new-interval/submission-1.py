class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        row = len(intervals)
        start,end = newInterval
        s,e=-1,-1
        for r in range(row):
            k,l = intervals[r][0], intervals[r][1]
            if start >= k and start<=l:
                s = k
            if end>=k and end <=l:
                e = l
        if s==-1: s=start
        if e==-1: e=end
        res = []
        for r in range(row):
            i,j = intervals[r][0], intervals[r][1]
            if not (j >= s and i <= e):
                res.append([i,j])
        res.append([s,e])
        res.sort()
        return res