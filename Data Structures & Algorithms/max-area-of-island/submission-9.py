class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def checkIsland(row, col):
            if row >= len(grid) or row < 0 or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0

            return 1 + checkIsland(row + 1, col) + checkIsland(row - 1, col) + checkIsland(row, col + 1) + checkIsland(row, col - 1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, checkIsland(row, col))
        
        return maxArea
                
