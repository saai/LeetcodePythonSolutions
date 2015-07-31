class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        n = len(s)
        s = s.lower()
        if n < 2:
            return True
        i = 0
        j = n-1
        while(i<=j):
            while(not s[i].isalnum() and i<j):
                i+=1
            while(not s[j].isalnum() and j>i):
                j -= 1
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True        