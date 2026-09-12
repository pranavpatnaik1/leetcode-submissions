class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        
        def dfs(row, col, depth):
            if depth == len(word):
                return True
            
            if (row < 0 or col < 0) or (row >= len(board) or col >= len(board[0])):
                return False
            if ((row, col) in visited) or (board[row][col] != word[depth]):
                return False
            
            visited.add((row, col))

            res = (dfs(row + 1, col , depth + 1) or
                dfs(row - 1, col, depth + 1) or
                dfs(row, col + 1, depth + 1) or
                dfs(row, col - 1, depth + 1))
            
                
            visited.remove((row, col))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        
        return False




        # down: [i + 1][j]
        # right: [i][j + 1]
        # left: [i][j - 1]
        # up: [i - 1][j]