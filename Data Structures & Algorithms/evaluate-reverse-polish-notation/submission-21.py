class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        stack = []

        for i in tokens:
            if i in ops:
                right = int(stack.pop())
                left = int(stack.pop())

                if i == "+":
                    stack.append(left + right)
                elif i == "-":
                    stack.append(left - right)
                elif i == "*":
                    stack.append(left * right)
                elif i == "/":
                    stack.append(left / right)
            
            else:
                stack.append(int(i))
        
        return int(stack[-1])