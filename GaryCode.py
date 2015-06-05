class Solution:
	def grayCode(self, n):
        if n < 1: return [0,]
        if n == 1: return [0,1]
        pre_bit = 1<<(n-1)
        lower = self.grayCode(n-1)
        return lower + [(pre_bit|i) for i in reversed(lower)]