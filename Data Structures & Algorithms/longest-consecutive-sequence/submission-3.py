class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Sort, then define a "sequence"
        nums = sorted(nums)
        print(nums)
        res = 1
        sequences = list()
        if not nums:
            return 0
        for i in range(len(nums)):
            if i+1 <= (len(nums)-1) and nums[i+1] == nums[i]:
                continue
            if i+1 <= (len(nums)-1) and nums[i+1] == nums[i] + 1:
                res += 1
            elif i+1 <= (len(nums)-1) and nums[i+1] != nums[i] + 1:
                sequences.append(res)
                res = 1

            if i == len(nums) - 1:
                sequences.append(res)
        return max(sequences)

        