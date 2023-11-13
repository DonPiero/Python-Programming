class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

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


myQueue = Queue()
myQueue.push(5)

print("Peek:", myQueue.peek())
print("Pop:", myQueue.pop())
print("Pop:", myQueue.pop())
print("Peek:", myQueue.peek())
