class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n == 0:
            return 1
        if n < 0:
            n *= -1
            x = 1/x
        return x*self.myPow(x*x,n/2) if n%2 else self.myPow(x*x,n/2)
        
    def myPow2(self,x,n):
        if n < 0:
            n *= -1
            x = 1/x
        res = 1
        while(n>0):
            if n%2 :
                res *= x
            x *= x
            n >>= 1 # divide 2 
        return res