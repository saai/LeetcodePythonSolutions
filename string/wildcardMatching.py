class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        if n == 0:
            return m == 0
        i = 0
        j = 0
        star = -1
        ss = -1
        while i < m:
            if j < n and (s[i]==p[j] or p[j] == '?'):
                i += 1
                j += 1
                continue
            if j < n and p[j]=='*':
                star = j
                ss = i
                j += 1
                continue
            if star >= 0:
                j = star + 1
                ss += 1
                i = ss
                continue
            return False
            
        while j < n and p[j] == '*':
            j += 1
        return j == n