class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        out = []
        while i < len(numbers):
            j = i + 1
            while j < len(numbers):
                if(numbers[i]+numbers[j]==target):
                    return [i+1,j+1]
                else:
                    j = j + 1
            i =i + 1