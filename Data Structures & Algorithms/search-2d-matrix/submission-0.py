class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        mid = (r + l) // 2

        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                break
            
        
        col = matrix[mid]
        l, r = 0, len(col) - 1
        while l <= r:
            guess = (l + r) // 2
            if col[guess] == target:
                return True
            elif col[guess] < target:
                l = guess + 1
            elif col[guess] > target:
                r = guess - 1
        
        return False

            
        