class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        r = 0
        for i in xrange(32):
            m=1<<(31-i)
            r = r^(1<<i if m&n>0 else 0)
        return r    