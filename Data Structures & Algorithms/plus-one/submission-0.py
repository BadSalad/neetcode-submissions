class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num =""
        for d in digits:
            num += str(d)
        num = int(num)
        num+=1
        num = str(num)
        res =[]
        for n in num:
            res.append(n)
        return res