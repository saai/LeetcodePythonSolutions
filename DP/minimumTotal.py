class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        n = len(triangle)
        row = [0 for i in xrange(n)]
        row[0] = triangle[0][0]
        for i in range(1,n):
            m = i+1
            pre = row[0] + triangle[i][0]
            for j in range(1,m):
                cur = min(row[j-1],(sys.maxint if j==m-1 else row[j])) + triangle[i][j]
                if j-1 >= 0: 
                    row[j-1] = pre
                pre = cur
            row[m-1] = pre
        return min(row)
                    