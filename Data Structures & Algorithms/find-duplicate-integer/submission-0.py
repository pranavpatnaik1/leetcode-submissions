class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ref = set()
        for i in range(len(nums)):
            if nums[i] in ref:
                return nums[i]
            ref.add(nums[i])

        
        