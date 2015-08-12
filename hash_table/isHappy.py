class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        sums = []
        val = self.calculateSums(n)
        while(val not in sums):
            if (val == 1) or (val/10 == 1 and (val- (val/10)*10)==0):
                return True
            sums.append(val)
            val = self.calculateSums(val)
        return False
        
    def calculateSums(self, n):
        total = 0
        while(n!=0):
            total += (n%10)**2
            n /= 10
        return total