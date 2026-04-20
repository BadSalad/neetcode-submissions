class Solution:
    def countSubstrings(self, s: str) -> int:
        out=0
        c = len(s)-1
        while c > -1:
            r = 0
            l = c
            while l < len(s):
                st = s[r:l+1]
                if st == st[::-1]:
                    out+=1
                r+=1
                l+=1
            c-=1
        return out