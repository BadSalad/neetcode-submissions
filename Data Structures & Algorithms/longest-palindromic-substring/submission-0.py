class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal(st):
            l,r=0,len(st)-1
            while l<r:
                if(st[l]!=st[r]):
                    return False
                l+=1
                r-=1
            return True
        max = 0
        out=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                k=s[i:j+1]
                if pal(k):
                    if len(k)>max:
                        max = len(k)
                        out=k
        
        return out