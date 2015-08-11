class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        if divisor == 0:
            return None
        sig = 1-2*(1 if dividend * divisor<0 else 0)
        dividend,divisor = abs(dividend), abs(divisor)
        if divisor == 1:
            return min(max(dividend * sig,-2147483648),2147483647)
        res = 0
        while(dividend >= divisor):
            t_divisor,i = divisor,1
            while(dividend >= t_divisor):
                dividend -= t_divisor
                res += i
                i <<=1 #i * 2 (twice each divisor, so twice the counter )
                t_divisor <<=1 # t_divisor *2 (increase divisor)
                
        return min(max(res * sig, -2147483648),2147483647)
        