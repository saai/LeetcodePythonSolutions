class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        nums = [i+1 for i in xrange(n)]
        facts = [0 for i in xrange(n)]
        facts[0] = 1
        for i in range(1,n):
            facts[i] = i*facts[i-1]
        k = k-1
        res = []
        for i in range(n,0,-1):
            idx = k/facts[i-1]
            k =  k%facts[i-1]
            res.append(nums[idx])
            nums.pop(idx)
        return ''.join([str(i) for i in res])