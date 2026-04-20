class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo ={}
        def pal(st):
            if st in memo:
                return memo[st]
            # l,r=0,len(st)-1
            # while l<r:
            #     if(st[l]!=st[r]):
            #         memo[st] = False
            #         return False
            #     l+=1
            #     r-=1
            # memo[st] = True
            # return True
            if st == st[::-1]:
                memo[st] = True
                return True
            memo[st] = False
            return False
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