class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # all trailing zeroes from 2 * 5 ,just find the number of factor 5 .
        return 0 if n == 0 else n / 5 + self.trailingZeroes(n / 5)