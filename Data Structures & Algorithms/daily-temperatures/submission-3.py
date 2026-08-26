class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # keep track of streak length of decreasing
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        
        return res