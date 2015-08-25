class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        st = []
        n = len(path)
        i = 1
        while(i<n):
            j = i 
            while(j<n and path[j] != '/'):
                j += 1
            s = path[i:j]
            if s == '':
                i += 1
            elif s == '.' :
                i = j
            elif s == '..':
                if len(st)>0:
                    st.pop()
                i = j
            else:
                st.append(s)
                i = j
        return '/'+'/'.join(st)
                