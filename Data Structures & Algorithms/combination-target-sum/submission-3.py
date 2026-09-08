class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()  # 1. Sort to enable early pruning
        
        def findComb(pos, remaining, path):
            if remaining == 0:
                res.append(path.copy())  # Make a snapshot of the valid path
                return
            
            for i in range(pos, len(nums)):
                # Prune: if current number exceeds remaining target, 
                # all subsequent numbers will too since nums is sorted.
                if nums[i] > remaining:
                    break
                
                path.append(nums[i])
                findComb(i, remaining - nums[i], path)  # Pass 'i' to allow duplicate numbers
                path.pop()  # Backtrack in-place
                
        findComb(0, target, [])
        return res