class Solution:
    def longestPalindrome(self, s: str) -> str:
        c = len(s)-1
        while c > 0:
            r = 0
            l = c
            while l < len(s):
                st = s[r:l+1]
                if st == st[::-1]:
                    return st
                r+=1
                l+=1
            c-=1
        return s[0]