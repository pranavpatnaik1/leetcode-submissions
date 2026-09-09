class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        def findSubsets(currList, pos):
            if pos >= len(nums):
                res.add(tuple(currList.copy()))
                return
            
            findSubsets(currList + [nums[pos]], pos + 1) # take it
            findSubsets(currList, pos + 1) # leave it
        
        findSubsets([], 0)
        res = [list(item) for item in res]
        return res