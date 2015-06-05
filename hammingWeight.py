class Solution:
	def hammingWeight(self, n):
        if n == 0:
            return 0
        hw = 0
        while (n != 0) :
            if n&1 == 1:
                hw+=1
            n=n>>1        
        return hw
    