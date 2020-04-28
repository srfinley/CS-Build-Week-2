# https://leetcode.com/problems/implement-queue-using-stacks/

class Stack:
    def __init__(self):
        self.storage = []
        
    def push_to_top(self, value):
        self.storage.append(value)
        
    def pop_from_top(self):
        value = self.storage[-1]
        self.storage = self.storage[:-1]
        return value
    
    def peek_at_top(self):
        return self.storage[-1]
    
    def size(self):
        return len(self.storage)
    
    def is_empty(self):
        return self.size() == 0

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = Stack()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        temp = []
        while not self.stack.is_empty():
            temp.append(self.stack.pop_from_top())
        self.stack.push_to_top(x)
        for value in temp[::-1]:
            self.stack.push_to_top(value)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop_from_top()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack.peek_at_top()
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack.is_empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()