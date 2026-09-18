import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceMap = dict()
        for point in points:
            x, y = point[0], point[1]
            dist = sqrt(x ** 2 + y ** 2)
            if dist in distanceMap:
                distanceMap[dist].append(point)
            else:
                distanceMap[dist] = [point]
        
        distHeap = list(distanceMap.keys())
        heapq.heapify(distHeap)

        res = []
        while len(res) < k:
            curr = heapq.heappop(distHeap)
            for j in distanceMap[curr]:
                res.append(j)
        
        return res
