class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ref = set()
        for i in range(len(nums)):
            ref.add(nums[i])
        
        return len(nums) != len(ref)