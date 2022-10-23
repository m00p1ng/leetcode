class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        helperStack = []
        while self.stack:
            helperStack.append(self.stack.pop())

        helperStack.append(x)

        while helperStack:
            self.stack.append(helperStack.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MyQueue()
    obj.push(10)
    param_2 = obj.pop()
    # param_3 = obj.peek()
    param_4 = obj.empty()

    print(param_2)
    # print(param_3)
    print(param_4)
