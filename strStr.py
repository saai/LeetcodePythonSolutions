class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        i = 0
        n = len(haystack)
        m = len(needle)
        if m<=0 and n == 0:
            return 0
        elif n<=0:
            return -1
        elif m <=0:
            return 0
        while(i < n-m+1):
            if haystack[i:i+m] == needle:
                    return i
            i+=1
        return -1