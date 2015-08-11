class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        m = len(t)
        n = len(s)
        if n == 0 or m == 0:
            return ""
        count = m
        min_len = n +1
        min_idx = 0
        required = {}
        for c in t:
            if c in required:
                required[c] += 1
            else:
                required[c] = 1
        i = -1
        j = 0
        while(i<n and j < n):
            if count:
                i += 1
                if i < n and s[i] in required:
                    required[s[i]] -= 1
                    if required[s[i]] >= 0:
                        count -= 1
            else:
                if (min_len > i-j+1):
                    min_len = i-j+1
                    min_idx = j
                if s[j] in required:
                    required[s[j]] += 1
                    if required[s[j]]>0:
                        count += 1
                j += 1
        if min_len == n+1:
            return ""
        return s[min_idx:min_idx+min_len]