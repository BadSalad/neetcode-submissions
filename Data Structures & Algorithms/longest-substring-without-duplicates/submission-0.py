# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         #This is a slding window problem
#         #Its a great algorithm but you have to think carefully
#         #It builds on top of 2 pointers
        
#         l = 0                           #Left Pointer
#         charSet = set()                 #To store unique values
#         out = 0
#         for r in range(len(s)):         #r is the right pointer
#             while s[r] not in charSet:
#                 charSet.remove(s[l])    #Remove the value at left pointer
#                 l += 1
#             charSet.add(s[r])
#             out = max(out,r-l+1)        #r-1+1 is the length of the substring

#         return out
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
        