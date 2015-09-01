class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.min = long(0)

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.st:
            self.st.append( x - self.mini)
            if x < self.mini:
                self.mini = x
        else:
            self.st.append(long(0))
            self.mini =long(x)
            
    def pop(self):
        """
        :rtype: nothing
        """
        if self.st:
            v = self.st.pop()
            if v < 0:
                self.mini -= v
            
    def top(self):
        """
        :rtype: int
        """
        v = self.st[-1]
        if v > 0:
            return int (v + self.mini)
        else:
            return int(self.mini)
    def getMin(self):
        """
        :rtype: int
        """
        return int(self.mini)
        