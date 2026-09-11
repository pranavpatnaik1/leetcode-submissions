from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        freshFruit = 0
        queue = deque()

        currMin = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    freshFruit += 1
                if grid[row][col] == 2:
                    queue.append([row, col])
        
        if freshFruit == 0:
            return 0

        while queue:
            lenQ = len(queue)
            for _ in range(lenQ):
                node = queue.popleft()
                row = node[0]
                col = node[1]

                for dr, dc in dirs:
                    new_row = row + dr
                    new_col = col + dc

                    if new_row < 0 or new_row >= len(grid):
                        continue
                        
                    if new_col < 0 or new_col >= len(grid[0]):
                        continue
                    
                    if grid[new_row][new_col] == 2:
                        continue
                        
                    if grid[new_row][new_col] == 1:
                        freshFruit -= 1
                        grid[new_row][new_col] = 2
                        queue.append([new_row, new_col])
                
            currMin += 1
        
       

        if freshFruit == 0:
            return currMin - 1
        else:
            return -1
        
                
            