class MinStack:

    def __init__(self):
        self.minStack = []
        self.mins = []
        self.currMin = 2**31 - 1

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if self.currMin >= val:
            self.currMin = val
            self.mins.append(val)
        

    def pop(self) -> None:
        if self.minStack.pop() == self.currMin:
            self.mins.pop()
            if self.mins:
                self.currMin = self.mins[-1]
            else:
                self.currMin = 2**31 - 1


    def top(self) -> int:
        return self.minStack[-1]
        

    def getMin(self) -> int:
        return self.currMin
        
