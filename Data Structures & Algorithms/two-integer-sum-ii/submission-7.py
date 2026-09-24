class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        sumSoln = numbers[l] + numbers[r]

        while sumSoln != target:
            if sumSoln < target:
                l += 1
            else:
                r -= 1
            
            sumSoln = numbers[l] + numbers[r]
        
        return [l+1, r+1]