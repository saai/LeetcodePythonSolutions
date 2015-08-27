class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        num = 0
        sign = '+'
        for i in xrange(len(s)):
            c = s[i]
            if ord(c)>= ord('0') and ord(c)<=ord('9'):
                num = num * 10 + int(c)
            if (c!=' ' and (ord(c)>ord('9') or ord(c)<ord('0'))) or i==len(s)-1:
                if sign == '+':
                    st.append(num)
                elif sign == '-':
                    st.append(-num)
                elif sign == '*':
                    st.append(st.pop()*num)
                elif sign == '/':
                    v = st.pop()
                    st.append(abs(v)/num *(1 if v > 0 else -1))
                sign = c
                num = 0
        res = 0
        for v in st:
            res += v
        return res