from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def canFinish(speed: int) -> bool:
            hours = 0
            for pile in piles:
                hours += ceil(pile / speed)
            
            return hours <= h
        
        while l <= r:
            mid = (l + r) // 2
            if canFinish(mid):
                answer = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return answer


        



        