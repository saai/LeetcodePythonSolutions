class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        p1 = 0
        p2 = 0
        p3 = 0
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1+l2 != l3:
            return False
        t = [[True for j in xrange(l2+1)] for i in xrange(l1+1)]
        for i in xrange(l1+1):
            for j in xrange(l2+1):
                if i==0 and j == 0:
                    t[i][j] = True
                elif i == 0:
                    t[i][j] = t[i][j-1] and (s2[j-1] == s3[j-1])
                elif j == 0:
                    t[i][j] = t[i-1][j] and (s1[i-1] == s3[i-1])
                else:
                    t[i][j] = (t[i][j-1] and s2[j-1] == s3[i+j-1]) or (t[i-1][j] and s1[i-1] == s3[i+j-1])
        return t[l1][l2]
                    