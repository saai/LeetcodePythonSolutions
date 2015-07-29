class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        l1 = len(word1)
        l2 = len(word2)
        a = [0 for j in xrange(l2+1)]
        for j in range(1,l2+1):
            a[j] = j
        for i in range(1,l1+1):
            prev = i
            for j in range(1,l2+1):
                cur = None
                if word1[i-1] == word2[j-1]:
                    cur = a[j-1]
                else:
                    cur = min(a[j],a[j-1],prev)+1
                a[j-1] = prev
                prev = cur
            a[l2] = prev
        return a[l2]