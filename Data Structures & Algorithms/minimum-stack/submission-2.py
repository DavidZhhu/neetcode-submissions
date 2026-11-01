class MinStack:

    def __init__(self):
        self.list = []
        self.index = 0
        self.length = 0

    def push(self, val: int) -> None:
        self.list.append(val)
        self.length += 1

    def pop(self) -> None:
        self.list.pop()
        self.length -= 1

    def top(self) -> int:
        return self.list[self.length-1]

    def getMin(self) -> int:
        return min(self.list)
        
