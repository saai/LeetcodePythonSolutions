class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        m = len(s)
        n = len(words)
        res = []
        if n == 0:
            return []
        wl = len(words[0])
        s_dict ={}
        for w in words:
            if w in s_dict:
                s_dict[w] += 1
            else:
                s_dict[w] = 1
        for i in xrange(wl):
            d = {}
            count = 0
            left = i
            for j in range(i,m-wl+1,wl):
                sub_s = s[j:j+wl]
                if sub_s in s_dict:
                    if sub_s not in d:
                        d[sub_s] = 1
                    else:
                        d[sub_s] += 1
                    count += 1
                    while d[sub_s] > s_dict[sub_s]:
                        d[s[left:left+wl]] -= 1
                        left += wl
                        count -= 1
                    if count == n:
                        res.append(left)
                else:
                    left = j + wl
                    d = {}
                    count = 0
        return res