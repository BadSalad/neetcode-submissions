class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #To maximise(j-i)*height[i||j]
        i = 0
        j = len(heights)-1
        
        mvol = 0
        while(i<j):
            if(heights[i]>=heights[j]):
                vol = (j-i)*(heights[j])
                j = j-1
            else:
                vol = (j-i)*heights[i]
                i = i+1
            
            if(vol > mvol):
                mvol = vol
        return mvol