class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = nums.copy()
        res = list()
        for i in range(len(temp)):
            temp[0], temp[i] = temp[i], temp[0]
            prod = 1
            for j in range(1, len(temp)):
                prod *= temp[j]
            res.append(prod)
        return res