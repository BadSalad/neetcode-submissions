class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.replace(" ","").lower()
        i = 0
        j = len(s)-1
        while i<j:
            if('a' <= s[i] <='z' or '0' <= s[i] <='9'):
                if('a' <= s[j] < 'z' or '0' <= s[j] < '9'):
                    if(s[i]!=s[j]):
                        return False
                    else:
                        i = i+ 1
                        j = j-1
                else:
                    j = j-1
            else:
                i=i +1
        return True