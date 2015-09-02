class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.st.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.st)>0:
            self.st = self.st[1:]
        

    def peek(self):
        """
        :rtype: int
        """
        if len(self.st)> 0:
            return self.st[0]
        else:
            return 0

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.st) == 0
        