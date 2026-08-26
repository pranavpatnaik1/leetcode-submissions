class Solution:
    def isValid(self, s: str) -> bool:
        ref = {']': '[', ')': '(', '}': '{'}
        stack = []

        for i in s:
            if i not in ref:
                stack.append(i)
            else:
                if len(stack) > 0 and ref[i] == stack.pop():
                    continue
                else:
                    return False
            
        return len(stack) == 0