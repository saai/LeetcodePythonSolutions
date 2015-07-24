class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        result = []
        numerators = []
        def fraction(numer,denom):
            if numer in numerators:
                index = numerators.index(numer)
                i = 0
                n = len(result)
                while result[i] != '.':
                    i += 1
                i+=1
                result.insert(index+i,'(')
                result.append(')')
                return 
            else:
                numerators.append(numer)
                num = numer/denom
                rest = numer%denom
                result.append(str(num))
                if rest ==0:
                    return
                else:
                    rest = rest*10
                    fraction(rest, denom)
        if numerator * denominator < 0:
            result.append('-')
        n = abs(numerator)/abs(denominator)
        r = abs(numerator)%abs(denominator)
        result.append(str(n))
        if r == 0:
            return "".join(result)
        else:
            result.append('.')
            r = r*10
            fraction(r,abs(denominator))
        return "".join(result)
        