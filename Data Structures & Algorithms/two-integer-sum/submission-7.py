class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(n)
        ref = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in ref:
                return [ref[diff], i]
            else:
                ref[nums[i]] = i


        # O(n^2)
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in nums and i != nums.index(diff):
        #         return [i, nums.index(diff)]

        