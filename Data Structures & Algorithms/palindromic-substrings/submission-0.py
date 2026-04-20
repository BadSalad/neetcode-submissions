class Solution:
    def countSubstrings(self, s: str) -> int:
        memo ={}
        def pal(st):
            if st == st[::-1]:
                return True
            return False
        c = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                k=s[i:j+1]
                if pal(k):
                    c+=1
        
        return c