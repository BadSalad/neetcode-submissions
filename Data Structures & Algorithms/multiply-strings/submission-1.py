class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1,l2 = len(num1),len(num2)
        n1,n2 =0,0
        for i in range(l1):
            d = ord(num1[i]) - ord("0")
            n1 += d*(10**(l1-(i+1)))
        for j in range(l2):
            e = ord(num2[j]) - ord("0")
            n2 += e*(10**(l2-(j+1)))
        res = n1*n2
        out = ""
        if res == 0: return "0"
        while res >0:
            d1 = res%10
            out = f"{d1}{out}"
            res = res//10
        return out