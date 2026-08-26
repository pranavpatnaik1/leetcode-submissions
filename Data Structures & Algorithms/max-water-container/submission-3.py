class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = -1
        currArea = (r - l) * min(heights[l], heights[r])
        maxArea = max(currArea, maxArea)

        while l <= r:
            if heights[l] >= heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1

            maxArea = max((r - l) * min(heights[l], heights[r]), maxArea)
        
        return maxArea