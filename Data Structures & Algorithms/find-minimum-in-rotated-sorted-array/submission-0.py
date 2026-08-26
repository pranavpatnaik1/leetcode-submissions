class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else: #Then, we know mid to r is sorted properly.
                r = mid
        
        return nums[l]