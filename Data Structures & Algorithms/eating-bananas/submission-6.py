class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        def time_taken(rate):
            time = 0
            for j in piles:
                time += math.ceil(j/rate)
            return time

        l = 1
        r = piles[-1]+1
        while l <= r:
            m = (l+r)//2
            hours = time_taken(m)
            if(hours>h):
                l = m + 1
            elif(hours<=h):
                r = m - 1
        return l