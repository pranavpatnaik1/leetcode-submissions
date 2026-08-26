class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l <= r:
            ref = numbers[l] + numbers[r]
            if ref == target:
                return [l+1, r+1]
            elif ref < target:
                l += 1
            elif ref > target:
                r -= 1
        

        