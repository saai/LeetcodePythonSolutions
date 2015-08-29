class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        factor2 = 2
        factor3 = 3
        factor5 = 5
        idx2 = 0
        idx3 = 0
        idx5 = 0
        for i in range(1,n):
            minv = min(factor2,factor3,factor5)
            res.append(minv) 
            if minv == factor2:
                idx2 += 1
                factor2 = res[idx2]*2
            if minv == factor3:
                idx3 += 1
                factor3 = res[idx3]*3
            if minv == factor5:
                idx5 += 1
                factor5 = res[idx5]*5
        return res[n-1]