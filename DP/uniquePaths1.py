class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        row = [1 for j in xrange(n)] # the 0th row
        for i in range(1,m):
            for j in range(1,n):
                cur = row[j-1] + row[j]
                row[j] = cur    
        return row[n-1]