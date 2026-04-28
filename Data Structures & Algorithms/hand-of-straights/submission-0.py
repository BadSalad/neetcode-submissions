class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize !=0: 
            return False
        hSet = [0] *1010
        ma = 0
        mi = 1000
        for h in hand:
            if h>ma: ma=h
            if h<mi: mi=h
            hSet[h] +=1
        
        while True: 
            for i in range(groupSize):
                if hSet[mi+i] == 0:
                    return False
                hSet[mi+i] -= 1
            c=1
            for j in range(ma+1):
                if hSet[j]>0: 
                    c=0
                    mi=j
                    break
            if c: break 
        return True