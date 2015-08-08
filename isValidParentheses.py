class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        st = []
        pair = {')':'(', '}':'{',']':'['}
        for c in s:
            if c in pair:
                if len(st) == 0:
                    return False
                elif st[-1] != pair[c]:
                    return False
                else:
                    st.pop()
                    continue
            st.append(c)
        return len(st)==0
        