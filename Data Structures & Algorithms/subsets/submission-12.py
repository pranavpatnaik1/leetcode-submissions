class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Construct decision tree
        res = []
        currList = []
        
        def dfs(currList: list, currPos: int):
            if currPos == len(nums):
                res.append(currList)
                return
            
            dfs(currList + [nums[currPos]], currPos + 1) # take it
            dfs(currList, currPos + 1) # leave it


        dfs(currList, 0)
        return res