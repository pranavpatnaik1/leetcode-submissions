class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ref = set(nums)
        streak = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in ref:
                start = nums[i]
                currStreak = 1
                while start + 1 in ref:
                    currStreak += 1
                    start += 1
            
                streak = max(currStreak, streak)
        
        return streak
                    
