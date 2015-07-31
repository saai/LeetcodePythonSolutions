class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        n = len(s)
        if n <2:
            return s
        longest = 1
        begin, start, end = 0,0,0
        # begin is the iterative center of possible palindrome in s
        while(begin <= n/2):
            start = end = begin
            while(end <n-1 and s[end+1] == s[end]):
                end += 1
            begin = end + 1 # next center
            while(end < n-1 and start >0 and s[end+1] == s[start -1]):
                end += 1
                start -= 1
            if start == 0 and longest < (end-start+1):
                longest = end-start+1
        remain = s[longest: n]
        return remain[::-1] + s
            