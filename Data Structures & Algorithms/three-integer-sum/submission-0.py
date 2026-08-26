class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlogn)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -(nums[i])
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                        
                    l += 1
                    r -= 1
                if s < target:
                    l += 1
                if s > target:
                    r -= 1
        
        return res