class Solution:
    # @param {string} s
    # @return {string[][]}
    def partition(self, s):
        indexes = {} # all palindromes
        n = len(s)
        if n < 2:
            return [[s]]
        begin, start , end = 0,0,0
        while(begin < n):
            start = end = begin
            while(end <n-1 and s[end+1] == s[end]):
                end += 1
            while(start >0 and end < n-1 and s[end+1] == s[start -1]):
                end += 1
                start -=1
            print start,end
            indexes[start] = end 
            begin = end + 1
        return indexes          
