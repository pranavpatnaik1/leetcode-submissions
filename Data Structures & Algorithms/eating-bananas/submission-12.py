from math import ceil
import copy

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        optimalRate = 2**31 + 1

        while l <= r:
            rate = (l + r) // 2

            # Simulate Koko eating bananas
            currHours = 0
            for i in piles:
                currHours += ceil(i/rate)
            
            if currHours <= h:
                if rate > optimalRate:
                    return optimalRate
                optimalRate = min(optimalRate, rate)
                r = rate - 1
            else:
                l = rate + 1
        
        return optimalRate

                

