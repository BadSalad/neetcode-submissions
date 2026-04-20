class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashs = [0]*2000
        h= [0]*2000
        for n in nums:
            hashs[n+1000] += 1
            h[n+1000] +=1

        h.sort()
        h = h[-k:]

        out = [0]*k
        c = 0
        for i in range(len(hashs)):
            if hashs[i] in h:
                out[c] = i-1000
                c+=1

        return out