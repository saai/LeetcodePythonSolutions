class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        pre1 = 2
        pre2 = 1
        cur = 0
        while(n>2):
            cur = pre1 + pre2
            pre2 = pre1
            pre1 = cur
            n -= 1
        return cur
        