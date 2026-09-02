class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # ref = set()
        # for i in range(len(nums)):
        #     if nums[i] in ref:
        #         return nums[i]
        #     ref.add(nums[i])

        fast, slow = 0, 0
        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]   
            fast = nums[nums[fast]]
        
        third = 0
        while slow != third:
            slow = nums[slow]
            third = nums[third]
        
        return slow
