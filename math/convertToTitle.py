class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        while(n>0):
            res.append(chr(ord('A')+(n-1)%26))
            n-=1
            n /= 26
        return ''.join(res[::-1])
        