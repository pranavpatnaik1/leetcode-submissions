class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # ittle tip: create a dirs variable = [(-1,0), (1,0)...] for each direction and and then for dr, dc in dirs to easily add the change of direction for your function call

        maxArea = 0
        dirs = [(-1, 0), (1,0), (0, 1), (0,-1)]

        def checkIsland(row, col):
            if row >= len(grid) or row < 0 or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            currArea = 0
            for dr, dc in dirs:
                currArea += checkIsland(row + dr, col + dc)
            
            return currArea + 1
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, checkIsland(row, col))
        
        return maxArea
                
