class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newlst = list()
        for i in range(len(nums)):
            if nums[i] in newlst:
                return True
            newlst.append(nums[i])
        
        return False
         