from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def checkSteps(currSteps) -> int:
            if currSteps < 0:
                return 0
            
            if currSteps == 0:
                return 1
            
            take = checkSteps(currSteps - 1)
            skip = checkSteps(currSteps - 2)

            return take + skip
        
        return checkSteps(n)

            
