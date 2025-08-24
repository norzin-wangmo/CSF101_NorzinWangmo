## Implementing a Stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)
    
# Test the stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  #  should print 3
print(stack.peek()) # should print 2
print(stack.size()) # should print 2