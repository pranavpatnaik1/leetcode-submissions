class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # Find minimum first.
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        minimum = l
        if minimum != 0:
            sortedNums = nums[minimum:] + nums[0:minimum]
        else:
            sortedNums = nums
        
        # Conduct binary search on sorted list.
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if sortedNums[mid] > target:
                r = mid - 1
            elif sortedNums[mid] < target:
                l = mid + 1
            else:
                return (mid + minimum) % len(nums)
        
        return -1




