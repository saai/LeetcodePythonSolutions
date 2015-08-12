class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n<=1:
            return 0
        isPrimes = [True for i in xrange(n)]
        i = 2
        while(i*i < n):
            if isPrimes[i]:
                for j in range(i*i,n,i):
                    isPrimes[j] = False
            i += 1
        
        count = 0
        for i in range(2,n):
            if isPrimes[i]:
                count += 1
        return count    
        