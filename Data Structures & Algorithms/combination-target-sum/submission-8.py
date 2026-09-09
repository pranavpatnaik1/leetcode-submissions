class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def findCombination(currList, pos, remaining):
            if remaining == 0:
                res.append(currList)
                return
            
            if pos >= len(nums) or remaining < 0:
                return
            
            findCombination(currList + [nums[pos]], pos, remaining - nums[pos])
            findCombination(currList, pos + 1, remaining)
        
        findCombination([], 0, target)
        return res
