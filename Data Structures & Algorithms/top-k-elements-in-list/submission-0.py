from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        
        count = Counter(nums)

        res = [[] for _ in range(len(nums) + 1)]
        for key, value in count.items():
            res[value].append(key)
        
        out = []
        for j in range(len(res) - 1, 0, -1):
            out += res[j]
        
        return out[:k]
