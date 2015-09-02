class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = []
        op = {'+':operator.add, '-': operator.sub, '*':operator.mul, '/':operator.floordiv}
        for t in tokens:
            if t in '+-':
                rop = st.pop()
                lop = st.pop()
                v = op[t](lop,rop)
                st.append(v)
            elif t in '*/':
                rop = st.pop()
                lop = st.pop()
                sig = 1 - 2*(0 if rop * lop >=0 else 1)
                v = op[t](abs(lop),abs(rop)) * sig
                st.append(v)
            else:    
                st.append(int(t))
        return int(st[-1])