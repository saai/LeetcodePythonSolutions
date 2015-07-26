class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply1(self, num1, num2):
        n1 = len(num1)
        n2 = len(num2)
        (lnum,snum,ln,sn) = (num1,num2,n1,n2) if n1>n2 else (num2,num1,n2,n1)
        result = '0'
        i = sn-1
        while(i >=0):
            num = int(snum[i])
            sumstr = '0' 
            #for j in xrange(num):
                #sumstr = self.strAdd(sumstr,lnum)
            sumstr = self.singleMulti(lnum,num)
            zeroNum = sn-1-i
            while(zeroNum > 0):
                sumstr += '0'
                zeroNum -= 1
            result = self.strAdd(result,sumstr)
            i -= 1
        return result
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        n1 = len(num1)
        n2 = len(num2)
        r = ['0']*(n1+n2)
        i = n1 - 1
        while(i>=0):
            carry = 0
            j = n2-1
            while(j>=0):
                v = int(r[i+j+1])+ int(num1[i])*int(num2[j]) + carry
                r[i+j+1] = str(v%10) 
                carry = v / 10
                j-=1
            r[i]= str(carry)
            i-=1    
        for p in xrange(n1+n2):
            if r[p] != '0':
                return ''.join(r[p:n1+n2])
        return '0'
        
        
    def strAdd(self,num1,num2):
        if num1 == None:
            return num2
        if num2 == None:
            return num1
        result = []
        n1 = len(num1)
        n2 = len(num2)
        (lnum,snum,ln,sn) = (num1,num2,n1,n2) if n1>=n2 else (num2,num1,n2,n1)
        lnum = lnum[::-1]
        snum = snum[::-1]
        carry = 0
        zeros = ln-sn
        while(zeros>0):
            snum += '0'
            zeros -= 1
        for i in xrange(ln):
            vsum = int(lnum[i])+int(snum[i]) + carry
            vleft = vsum % 10
            carry = vsum /10
            result.append(str(vleft))
        if carry != 0:
            result.append(str(carry))
        result.reverse()
        return ''.join(result)
        
    def singleMulti(self, num1,int_n):
        if int_n == 0:
            return '0'
        result = []
        n = len(num1)
        num = num1[::-1]
        carry = 0
        for i in xrange(n):
            v = int(num[i])*int_n + carry
            vleft = v % 10
            carry = v/10
            result.append(str(vleft))
        if carry != 0:
            result.append(str(carry))
        result.reverse()
        return ''.join(result)