class Solution:
    def trap(self, height: List[int]) -> int:
        # maxLeft
        maxLeft = [0]
        currMax = 0
        for i in range(len(height)):
            if height[i] > currMax:
                currMax = height[i]
            maxLeft.append(currMax)

        maxRight = [0]
        currMax = 0
        for j in range(len(height) - 1, -1, -1):
            if height[j] > currMax:
                currMax = height[j]
            maxRight.append(currMax)
        
        maxRight.reverse()
        res = 0
        for k in range(len(height)):
            res += (max(min(maxLeft[k], maxRight[k]) - height[k], 0))
        
        print(maxRight, maxLeft)
        return res


                

            

            
            


        
