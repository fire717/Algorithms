# 还是没大懂题目意思
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
    
    def pop(self):
        """
        :rtype: nothing
        """
        if not self.empty:
            self.queue.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        if not self.empty:
            return self.queue.pop(0)
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue)==0
        
# 原来要用栈模拟。
class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        swap = []
        while self.stack:
            swap.append(self.stack.pop())
        swap.append(x)
        while swap:
            self.stack.append(swap.pop())

    # @return nothing
    def pop(self):
        self.stack.pop()

    # @return an integer
    def peek(self):
        return self.stack[-1]

    # @return an boolean
    def empty(self):
        return len(self.stack) == 0
