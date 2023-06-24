from collections import deque


class Stack:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.append(value)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
