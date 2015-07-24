class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue.append(x)

    # @return nothing
    def pop(self):
        n = len(self.queue)
        if n != 0:
            self.queue.pop(n-1)

    # @return an integer
    def top(self):
        n = len(self.queue)
        if n != 0:
            return self.queue[n-1]

    # @return an boolean
    def empty(self):
        n = len(self.queue)
        if n == 0:
            return True
        else:
            return False