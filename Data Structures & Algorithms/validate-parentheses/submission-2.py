class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'}': '{', ')': '(', ']': '['}

        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                if len(stack) > 0:
                    top = stack.pop()

                    if pairs[c] != top:
                        return False
                else:
                    return False
        
        return len(stack) == 0
        