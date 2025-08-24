# Implementing Stack using Queue
from queue import Queue

class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        self.q2.put(x)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.get()
    
    def top(self) -> int:
        return self.q1.queue[0]
    
    def empty(self) -> bool:
        return self.q1.empty()