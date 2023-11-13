class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not len(self.items) == 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not len(self.items) == 0:
            return self.items[-1]
        else:
            return None


myStack = Stack()
myStack.push(5)

print("Peek:", myStack.peek())
print("Pop:", myStack.pop())
print("Pop:", myStack.pop())
print("Peek:", myStack.peek())
