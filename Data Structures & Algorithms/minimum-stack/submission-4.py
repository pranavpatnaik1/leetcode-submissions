class MinStack:

    def __init__(self):
        self.stack = []
        self.ref = []
        self.minimum = 2**32 + 1
        

        
    def push(self, val: int) -> None:
        if val < self.minimum:
            self.minimum = val
        self.ref.append(self.minimum)
        self.stack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.ref.pop()
        
        # update minimum after popping
        if self.ref:
            self.minimum = self.ref[-1]
        else:
            self.minimum = 2**32 + 1
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.ref[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()