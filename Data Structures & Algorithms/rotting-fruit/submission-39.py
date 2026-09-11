from collections import deque
from math import sqrt

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        freshFruit = 0
        rottenQueue = deque()

        def rotFruit(queue):
            currMin = 0

            while queue:
                lenQ = len(queue)
                for _ in range(lenQ):
                    node = queue.popleft()
                    row = node[0]
                    col = node[1]

                    for dr, dc in dirs:
                        if row + dr < 0 or row + dr >= len(grid):
                            continue
                            
                        if col + dc < 0 or col + dc >= len(grid[0]):
                            continue
                        
                        if grid[row + dr][col + dc] == 2:
                            continue
                            
                        if grid[row + dr][col + dc] == 1:
                            nonlocal freshFruit
                            freshFruit -= 1
                            grid[row + dr][col + dc] = 2
                            queue.append([row + dr, col + dc])
                    
                currMin += 1
            
            return currMin

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    freshFruit += 1
                if grid[row][col] == 2:
                    rottenQueue.append([row, col])
        
        if len(rottenQueue) == 0 and freshFruit > 0:
            return -1
        if len(rottenQueue) == 0 and freshFruit == 0:
            return 0

        res = rotFruit(rottenQueue) - 1
        if freshFruit == 0:
            return res
        else:
            return -1
        
                
            