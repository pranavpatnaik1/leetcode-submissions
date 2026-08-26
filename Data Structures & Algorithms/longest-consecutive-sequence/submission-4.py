class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ref = set(nums)
        maxStreak = 0
        for num in ref:
            if (num - 1) in ref:
                continue
            streak = 1
            curr = num
            while (curr + 1) in ref:
                curr += 1
                streak += 1
            
            maxStreak = max(maxStreak, streak)
        
        return maxStreak


        