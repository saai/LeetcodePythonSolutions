class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        res = 0
        sign = 1
        num = 0
        for c in s:
            if ord(c)>=ord('0') and ord(c)<=ord('9'):
               num = num * 10 + int(c)
            elif c == '+':
                res += sign*num
                num = 0
                sign = 1
            elif c == '-':
                res += sign * num
                num = 0
                sign = -1
            elif c == '(':
                st.append(res)
                st.append(sign)
                sign = 1
                res = 0
                num = 0
            elif c == ')':
                res += sign * num
                res *= st.pop()
                res += st.pop()
                sign = 1
                num = 0
        res += sign * num
        return res