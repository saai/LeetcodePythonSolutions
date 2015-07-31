class Solution:
    def isPalindrome(self, s):
        n = len(s)
        if n ==0 or n ==1:
            return True
        i = 0
        j = n-1
        while(i<=j):
            if s[i]!=s[j]:
                print i, j,s[i],s[j]
                return False
            i+=1
            j-=1
        return True
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        n = len(s)
        if n == 0:
            return None
        if n == 1:
            return s
        b,e,i = 0,0,0
        max_len = 0
        while(i<n):
            l = 1
            while(l<=2):
                start = i+1-(max_len+l)
                if start < 0:
                    break
                substr = s[start:i+1]
                if self.isPalindrome(substr):
                    max_len = len(substr)
                    b = start
                    e = i+1
                l+=1
            i+=1
        return s[b:e]   