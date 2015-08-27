class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        pre1 = 1
        pre2 = 1
        cur = 0
        for i in xrange(n):
            if i == 0:
                if s[i] == '0':
                    return 0
                else:
                    cur = 1
            elif s[i] == '0' and s[i-1] == s[i]:
                return 0
            else:
                cur = (pre1 if s[i]!='0' else 0) + \
                      (pre2)*(1 if s[i-1]!= '0' and int(s[i-1:i+1])<=26 else 0)
                pre2 = pre1
                pre1 = cur
        return cur