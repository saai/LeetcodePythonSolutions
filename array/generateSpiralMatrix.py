class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        res = [[0 for j in xrange(n)] for i in xrange(n)]
        min_i = 0
        max_i = n-1
        min_j = 0
        max_j = n-1
        num = 1
        while(min_i<=max_i and min_j<=max_j):
            for j in range(min_j,max_j+1):
                res[min_i][j] = num
                num += 1
            min_i += 1
            for i in range(min_i, max_i+1):
                res[i][max_j] = num
                num+=1
            max_j -= 1
            if (min_i<=max_i):
                for j in range(max_j,min_j-1,-1):
                    res[max_i][j] = num
                    num+=1
                max_i -=1
            if (min_j<=max_j):
                for i in range(max_i,min_i-1,-1):
                    res[i][min_j] = num
                    num+=1
                min_j +=1
        return res