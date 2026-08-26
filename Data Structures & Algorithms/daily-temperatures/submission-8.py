class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            curr = temperatures[i]

            while stack and curr >= stack[-1][1]:
                stack.pop()
            
            if stack:
                res[i] = stack[-1][0] - i
            
            stack.append([i, curr])
        
        return res