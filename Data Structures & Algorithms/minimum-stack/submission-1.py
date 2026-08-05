class MinStack:

    def __init__(self):
        self.stack = list()
        self.dq = deque()
    def push(self, val: int) -> None:
        self.stack.append(val)
        if(self.dq and self.dq[-1] >= val or (not self.dq)): 
            self.dq.append(val)

    def pop(self) -> None:
        if (self.stack): t = self.stack.pop()
        if(self.dq and self.dq[-1] == t):
            self.dq.pop()
        return None

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.dq[-1] if self.dq else None
