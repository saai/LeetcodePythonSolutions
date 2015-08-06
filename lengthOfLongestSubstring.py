class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n <=1:
            return n
        start = 0
        max_count = 1
        c_dict = {s[0]:0}
        for p in range(1,n):
            sub = s[start:p]
            c = s[p]
            if c in sub:
                start = c_dict[c]+1
            c_dict[c]=p
            max_count = max(max_count , p-start+1)
        return max_count