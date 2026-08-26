class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ref = set()
        for i in nums:
            if i in ref:
                return True
            ref.add(i)
        
        return False