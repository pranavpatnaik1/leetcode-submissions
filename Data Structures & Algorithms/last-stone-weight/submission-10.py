import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first == second:
                continue
            elif first < second:
                heapq.heappush(stones, abs(first - second) * -1)

        if len(stones) == 0:
            return 0
        return abs(stones[0])