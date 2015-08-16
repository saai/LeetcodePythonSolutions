class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        nr = len(matrix)
        nc = len(matrix[0])
        col0 = 1
        for i in xrange(nr):
            if matrix[i][0] == 0: 
                col0 = 0
            for j in range(1,nc):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(nr-1,-1,-1):
            for j in range(nc-1,0,-1):
                if matrix[i][0]==0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0==0:
                matrix[i][0] = 0