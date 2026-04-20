class MinStack:

    def __init__(self):
        self.container =deque()
        

    def push(self, val: int) -> None:
        self.container.append(val)

    def pop(self) -> None:
        return self.container.pop()

    def top(self) -> int:
        return self.container[-1]

    def getMin(self) -> int:
        return min(self.container)
