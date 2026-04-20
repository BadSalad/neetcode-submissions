class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sod(num):
            su = 0
            while num > 0:
                d= num%10
                su+=d**2
                num=num//10
            return su
        
        s=n
        seen = set()
        while s:
            seen.add(s)
            s= sod(s)
            if s == 1: return True
            if s in seen: return False