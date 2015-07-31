class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        n = len(s)
        if n < 2:
            return 0
        cut = [i-1 for i in xrange(n+1)]
        for i in xrange(n):
            j = 0
            while(i-j>=0 and i+j<n and s[i-j] == s[i+j]): # odd num palindrome
                cut[i+j+1] = min(cut[i+j+1], 1+cut[i-j])
                j+=1
            j = 1
            while(i-j+1>=0 and i+j<n and s[i-j+1] == s[i+j]): # even num palindrome
                cut[i+j+1] = min(cut[i+j+1], 1+ cut[i-j+1])
                j+=1
        return cut[n]