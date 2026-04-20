class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            w = s1 - s2

            if -w:
                heapq.heappush(stones,w)

        if len(stones)>0:
            return -stones[0]
        else:
            return 0