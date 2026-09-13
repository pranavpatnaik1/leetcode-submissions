class Solution:
    def climbStairs(self, n: int) -> int:
        memo = dict()

        def checkSteps(currSteps) -> int:
            if currSteps < 0:
                return 0
            
            if currSteps == 0:
                return 1
            
            if currSteps in memo:
                return memo[currSteps]
            
            take = checkSteps(currSteps - 1)
            skip = checkSteps(currSteps - 2)

            memo[currSteps] = take + skip

            return memo[currSteps]
        
        return checkSteps(n)

            
