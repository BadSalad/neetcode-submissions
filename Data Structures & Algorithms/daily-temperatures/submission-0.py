class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        i = len(temperatures)-1
        res = []
        res.append(0)
        stack.append(temperatures[-1])
        i=i-1
        while(i>=0):
            temp = stack.copy()
            c=1
            k=0
            while temp:
                #k=1
                check =temp.pop()
                if(temperatures[i]<check):
                    k = 1
                    break
                c+=1
            if k: res.append(c)
            else: res.append(0)
            stack.append(temperatures[i])
            i-=1
        return res[::-1]
                            
                