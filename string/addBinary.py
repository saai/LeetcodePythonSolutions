class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = 0
        i = len(a)-1
        j = len(b)-1
        res = ''
        while(i>=0 or j>=0 or c):
            na = 0
            nb = 0
            if i>=0:
                na = int(a[i])
                i -= 1
            if j >= 0:
                nb = int(b[j])
                j -= 1
            res = str(c^na^nb)+res
            c = (na+nb+c)/2
        return res