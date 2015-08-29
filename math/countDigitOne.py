class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        m = 1
        r = 1
        while(n>0):
            res += (n+8)/10*m + (n%10==1)*r         
            r += n%10*m
            n/=10
            m *= 10
        return res            
                