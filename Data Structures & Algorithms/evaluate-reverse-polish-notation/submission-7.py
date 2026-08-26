class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in ops:
                op = tokens[i]
                second = stack.pop()
                first = stack.pop()
                if op == '+':
                    stack.append(first + second)
                elif op == '-':
                    stack.append(first - second)
                elif op == '*':
                    stack.append(first * second)
                elif op == '/':
                    stack.append(int(first / second))
            else:
                stack.append(int(tokens[i]))
            
        return stack[0]
        
        