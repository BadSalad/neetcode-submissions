class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hSet = [0]*26
        for l in s:
            hSet[ord(l)-ord('a')] +=1
        out = []
        seen = set()
        i = 0 
        prev = 0
        while i < len(s):
            seen.add(s[i])
            hSet[ord(s[i])-ord('a')] -=1
            if hSet[ord(s[i])-ord('a')] == 0:
                seen.remove(s[i])
            if len(seen) == 0:
                out.append(i+1-prev)
                prev = i+1
            i+=1
        return out