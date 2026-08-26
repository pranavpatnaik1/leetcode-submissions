class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for focus in tokens:
            if focus == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif focus == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif focus == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            elif focus == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(focus))
                
        
        return stack[0]


