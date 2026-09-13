class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = dict()

        def checkCost(pos):
            if pos >= len(cost):
                return 0

            if pos in memo:
                return memo[pos]

            take = checkCost(pos + 1)
            skip = checkCost(pos + 2)
            
            memo[pos] = cost[pos] + min(take, skip)
            return memo[pos]
        
        return min(checkCost(0), checkCost(1))

            
            
