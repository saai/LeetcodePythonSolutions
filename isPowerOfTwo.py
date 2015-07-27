class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n == 0 or n == 1:
            return True
        if n%2 != 0:
            return False
        next_n = n**(.5)
        print next_n 
        if next_n%1 != 0:
            print 'decimals' 
            return False 
        else:
            return self.isPowerOfTwo(next_n)
        
