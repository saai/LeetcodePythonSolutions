class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        n = len(s)
        if n < 10:
            return []
        sl = 10
        res = []
        d = {}
        for i in xrange(sl):
            for j in range(i,n - sl + 1, sl):
                seq = s[j:j+sl]
                if seq not in d:
                    d[seq] = 1
                else:
                    if seq not in res:
                        res.append(seq)
        return res
 