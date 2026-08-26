class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if board[r][c] == ".":
                    continue
                if (curr in rows[r] 
                or curr in cols[c]
                or curr in squares[(r//3,c//3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        return True

        