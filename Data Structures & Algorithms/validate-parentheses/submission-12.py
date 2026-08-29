class Solution:
    def isValid(self, s: str) -> bool:
        parens = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        stack = []
        for i in s:
            if i in parens:
                if stack and parens[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        print(stack)
        if stack:
            return False
        else:
            return True