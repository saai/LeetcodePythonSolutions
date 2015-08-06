class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        i = 0
        j = 0
        n = len(strs)
        if i >=n:
            return ""
        c = None
        while(i<n):
            l = len(strs[i])
            if j > l-1 or (c and strs[i][j] != c):
                break
            c = strs[i][j]
            if i == n-1:
                i = 0
                c = None
                j += 1
            else:
                i += 1
        return strs[i][:j]
            