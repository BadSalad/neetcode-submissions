class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = [0]*26
        for s in s1:
            count[ord(s)-ord("a")] += 1
        
        i = 0
        j = i + len(s1) - 1

        while(j<len(s2)):
            temp = s2[i:j+1]
            countS=[0]*26
            for s in temp:
                countS[ord(s)-ord("a")] += 1   
            i += 1
            j += 1
            if count == countS: return True

        return False 

        