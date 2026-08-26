class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        track = 1
        for i in range(len(nums)):
            prefix[i] = track
            track *= nums[i]
        
        suffix = [1] * len(nums)
        track = 1
        for j in range(len(nums) - 1, -1, -1):
            suffix[j] = track
            track *= nums[j]
        
        for k in range(len(suffix)):
            suffix[k] *= prefix[k]
        
        return suffix

        

        