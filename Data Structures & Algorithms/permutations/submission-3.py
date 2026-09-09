class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def findPermutations(currList, resList):
            if len(currList) == len(nums):
                res.append(currList)
                return
            
            print(currList)
            lenRes = len(resList)
            for i in range(lenRes):
                findPermutations(currList + [resList[i]], resList[:i] + resList[i+1:])
            
        
        findPermutations([], nums)
        return res
