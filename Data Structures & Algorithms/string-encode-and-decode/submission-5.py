class Solution:

    def encode(self, strs: List[str]) -> str:
        oneSTR = ""
        for s in strs:
            oneSTR += "#"+str(len(s))+"/"+s 
        return oneSTR

    def decode(self, s: str) -> List[str]:
        lis = []
        i=0
        temp =""
        while i < len(s):
            if(s[i]=='#' and '0'<=s[i+1]<='9'):
                k = i+1
                num = ""
                while(s[k] != '/'):
                    num += s[k]
                    k += 1
                temp = s[k+1:k+1+int(num)]
                lis.append(temp)
                i = k+1+int(num)
            else:
                i += 1
                
        return lis

