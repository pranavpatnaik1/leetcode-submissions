class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxRight = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                arr[i] = -1
            else:
                newMax = max(maxRight, arr[i])
                arr[i] = maxRight
                maxRight = newMax
        
        return arr