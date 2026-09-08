class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def findComb(currList, remaining, pos):
            if remaining == 0:
                res.append(currList)
                return
            if pos >= len(nums) or remaining < 0:
                return
            
            findComb(currList + [nums[pos]], remaining - nums[pos], pos)
            findComb(currList, remaining, pos + 1)
        
        findComb([], target, 0)
        return res

