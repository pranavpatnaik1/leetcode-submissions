class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in nums and i != nums.index(rest):
                if i < nums.index(rest):
                    return [i, nums.index(rest)]
                else:
                    return [nums.index(rest), i]
        