from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            rate = (l + r) // 2

            # Simulate Koko eating bananas
            currHours = 0
            for i in piles:
                currHours += ceil(i/rate)
            
            if currHours <= h:
                r = rate - 1
            else:
                l = rate + 1
        
        return l

                

